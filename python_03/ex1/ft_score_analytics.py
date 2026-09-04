import sys


def process_scores(scores: list[int]) -> None:
    i = 1
    while i < len(sys.argv):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1
    if len(scores) == 0:
        raise ValueError


if __name__ == "__main__":
    scores: list[int] = []
    print("=== Player Score Analytics ===")
    try:
        process_scores(scores)
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    except ValueError:
        print("No scores provided. Usage: python3 ", end='')
        print("ft_score_analytics.py <score1> <score2> ...")
    finally:
        print()
