from config import *
from analytics import Research


def main():
    reader = Research(filepath)
    num_observations = len(reader.data)
    heads, tails = reader.calc.count
    heads_prob, tails_prob = reader.calc.fraction
    pred = reader.calc.predict_random(num_steps)
    heads_pred, tails_pred = tuple(sum(elem) for elem in zip(*pred))
    text = template.format(
        num_observations,
        heads, tails,
        heads_prob, tails_prob,
        num_steps,
        heads_pred, tails_pred
        )
    reader.calc.save_file(text, output_file)


if __name__ == '__main__':
    main()
