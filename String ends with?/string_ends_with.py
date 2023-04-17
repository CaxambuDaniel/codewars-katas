def solution(text, ending):
    revert = text[-len(ending):][::-1]
    return True if revert == ending[::-1] else False

def main():
    text1 = "hello world"
    ending1 = "world"
    text2 = "python"
    ending2 = "on"
    text3 = "abcdef"
    ending3 = "gh"

    print(f"Solution for '{text1}' and '{ending1}': {solution(text1, ending1)}")
    print(f"Solution for '{text2}' and '{ending2}': {solution(text2, ending2)}")
    print(f"Solution for '{text3}' and '{ending3}': {solution(text3, ending3)}")

if __name__ == "__main__":
    main()
