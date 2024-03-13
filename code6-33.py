avg= 95.6
score = 85
print("1. ", 2<3 and 3<5, "\t", 2<3 and 3>5)
print("2. ", 2<3 or 3<5, "\t", 2>3 or 3<5, "\t", 2>3 or 3>5)
print("3. ", not(2<3 and 3<5), "\t", not(2>3 or 3<5))
print("4. ", not(56<=78), "\t", avg>=80 and avg<90)
print("5. ", 80<score and score<90)
print("6. ", "python"and 9>7 , "\t", 68 and 9>7)
print("7. ", 9>7 or 0, "\t", 0 and 9>7)
print("8. ", 9>7 and 10, "\t", 0 or 1)
print("9. ", "python"and 9>7 )
print("10. ", "python"and 5>7 )
print("11. ", 10 and 9>7)
print("12. ", 9>7 or 10, "\t", 10 or 9>7)  # or에서 모두가 참이면 젤 앞에꼐 나옴
print("13. ", 2>3 or 0, "\t", 0 or 2>3)    # or 에서 모두 거짓이면 젤 뒤에께 나옴
print("14. ", 2<3 and 10, "\t", 10 and 2<3) # and에서 모두 참이면 젤 뒤에께 나옴
print("15. ", 2>3 and 0, "\t", 0 and 2>3)   # and에서 모두 거짓이면 젤 앞에께 나옴
