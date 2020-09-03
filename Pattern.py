def draw_pattern(N, M):
    text = 'Anmol Sethi'
    pattern = [('.|.'*(2*i + 1)).center(M, '-') for i in range(N//2)]   
    print('\n'.join(pattern + [text.center(M, '-')] + pattern[::-1]))
    

if __name__ == "__main__":
    N, M = input().split()
    draw_pattern(int(N), int(M))