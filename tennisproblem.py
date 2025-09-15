
TIE_BREAK_CAP = 3
def is_game(score):
    if len(score) != 2:
        return False
    for i in range(len(score)):
        if score[i] not in ['0','15','30','40','Ad']:
            return False
        if score[i] == "Ad" and score[i - 1] != '40':
            return False
    return True
    
def is_set(score):
    if len(score) != 2:
        return [False, 0]
    try:
        p1, p2 = map(int, score)
    except ValueError:
        return [False, 0]
    min_score = min(p1, p2)
    max_score = max(p1, p2)
    if min_score < 0 or max_score > TIE_BREAK_CAP or min_score == TIE_BREAK_CAP:
        return [False, 0]
    # tran dau dang dien ra
    if max_score < 6:
        return [True, 0]   
    diff = max_score - min_score
    if diff > 2: 
        if max_score == 6:
            return [True, 1 if p1 > p2 else 2]
        else: 
            return [False, 0]
    elif diff == 2 or (max_score == TIE_BREAK_CAP and diff == 1):
        return [True, 1 if p1 > p2 else 2]
    else: 
        return [True, 0]
        
def is_match(str_score):
    list_score = []
    str_score = str_score.strip().split()
    if not 2 <= len(str_score) <= 4:
        return False
    for s in str_score:
        s = s.split('-')
        list_score.append(s)
    if is_game(list_score[-1]):
        winner = []
        set_score = list_score[:-1]
        match_type = [[2,1,0], [1,2,0], [1, 0], [2, 0], [0]]
        for s in set_score:
            s = is_set(s)
            if s[0] == True:
                winner.append(s[1])
            else: 
                return False
        if winner in match_type:
            return True
        else:
            return False
    else:  
        set_score = list_score
        set_type = [[1,1], [2,2], [1,2,1], [1,2,2], [2,1,1], [2,1,2]]
        set_winner = []
        for s in set_score:
            s = is_set(s)
            if s[0] == True:
                set_winner.append(s[1])
            else: 
                return False
        if set_winner in set_type:
            return True
        else:
            return False
def test_match_validation():
    """Test các trường hợp tennis match"""
    test_cases = [
        # Trận đấu đang diễn ra
        ("6-4 3-6 3-3 15-30", True, "Set 3 đang diễn ra + game hiện tại"),
        ("6-4 3-6 5-4 40-15", True, "Set 3 đang diễn ra + game hiện tại"),
        ("6-4 3-6 6-5 15-0", True, "Set 3 + game hiện tại"),
        ("6-4 3-6 6-6 40-Ad", True, "Tie-break + game hiện tại"),
        ("3-2 0-15", True, "Set đang diễn ra + game hiện tại"),
        ("0-0 0-0", True, "Game đầu tiên"),
        
        # Trận đấu đã kết thúc
        ("6-4 6-2", True, "Thắng 2-0"),
        ("6-4 3-6 6-3", True, "Thắng 2-1"),
        ("4-6 6-3 7-5", True, "Thắng 2-1"),
        
        # Trường hợp không hợp lệ
        ("6-4 3-6 3-3", False, "Thiếu game score cho trận chưa kết thúc"),
        ("6-4 3-6 5-4", False, "Thiếu game score cho trận chưa kết thúc"),
        ("3-2", False, "Thiếu game score cho set chưa kết thúc"),
        ("6-4 6-2 3-3", False, "Trận đã kết thúc nhưng vẫn có set 3"),
        ("6-4 6-2 30-15", False, "Trận đã kết thúc nhưng vẫn có game hiện tại"),
        ("6-4 6-3 7-5", False, "2 set đầu cùng người thắng nhưng vẫn có set 3"),
        ("7-5 6-4 6-2", False, "2 set đầu cùng người thắng nhưng vẫn có set 3"),
        ("6-4 30-15 3-6", False, "Game score không ở cuối"),
        ("6-4 3-3 6-2", False, "Set chưa kết thúc không ở cuối"),
        ("15-30", False, "Thiếu set score"),
        ("6-4 3-6", False, "Thiếu set 3 và game score"),
        
        
        # Lỗi format
        ("", False, "Chuỗi rỗng"),
        ("6-4-3", False, "Format sai"),
        ("6-4-", False, "Format sai"),
        ("6 4", False, "Thiếu dấu -"),
        ("6-a", False, "Điểm không hợp lệ"),
        ("6-4 3-6 6-5 45-30", False, "Game score không hợp lệ"),
        ("6-4 11-9", False, "Set score không hợp lệ"),
        ("30-Ad", False, "Format sai"),
        
        # Edge cases
        ("10-8", False, "Thiếu game score"),
        ("9-7 8-6", True, "Thắng 2 tie-break"),
        ("6-4 3-6 10-9", True, "10-9 thắng ở ngưỡng tối đa"),
    ]
    
    print("Tennis Match Validation Test:")
    print("=" * 70)
    
    passed = 0
    total = len(test_cases)
    
    for i, (match_str, expected, description) in enumerate(test_cases):
        result = is_match(match_str)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed += 1
        
        print(f"Test {i+1:2d}: {status}")
        print(f"  Input: '{match_str}'")
        print(f"  Expected: {expected}, Got: {result}")
        print(f"  {description}")
        
        if result != expected:
            print(f"  >>> MISMATCH! <<<")
        print()
    
    print("=" * 70)
    print(f"Results: {passed}/{total} tests passed")
    if passed == total:
        print("🎾 All tests passed! Tennis match validator is working correctly!")
    else:
        print(f"❌ {total - passed} tests failed. Please review the logic.")


if __name__ == "__main__":
    test_match_validation()
        
    
