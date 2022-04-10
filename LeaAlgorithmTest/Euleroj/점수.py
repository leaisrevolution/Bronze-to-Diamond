'''

점수 #1037

문제
호그와트 마법 학교의 학생 오일러와 헤르미온느는 네 개의 과목을 시험 본다. - 정보, 고양이로 변신할 수 있는 변신술, 어둠의 마법 방어술, 약초학

오일러의 네 과목의 총점을 S라고 하고, 헤르미온느의 네 과목의 총점을 T라고 할 때, S와 T 중에서 더 높은 점수를 구하여라. 만일 S와 T가 같다면 둘 중 어느 것을 선택해도 상관없다.

입력형식

입력은 모두 두 개의 줄로 구성된다. 첫째 줄에는 오일러의 정보, 변신술, 방어술, 약초학의 점수를 나타내는 네 개의 정수가 주어지고, 둘째 줄에는 헤르미온느의 정보, 변신술, 방어술, 약초학의 점수를 나타내는 네 개의 정수가 주어진다. 주어지는 점수는 모두 0 이상 100 이하의 정수이다.

출력형식

오일러와 헤르미온느의 총점 중에서 더 높은 점수를 첫째 줄에 출력하여라.

'''


a, b, c, d = map(int, input().split())
e, f, g, h = map(int, input().split())

S = a + b + c + d
T = e + f + g + h

if S > T:
    print(S)
elif S < T:
    print(T)
else:
    print(S)


