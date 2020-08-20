import logging
from config import *
from analytics import Research


def main():
    try:
        logging.info('Reading csv file')
        reader = Research(filepath)
        logging.info('Calculating necessary values')
        num_observations = len(reader.data)
        heads, tails = reader.calc.count
        heads_prob, tails_prob = reader.calc.fraction
        pred = reader.calc.predict_random(num_steps)
        heads_pred, tails_pred = tuple(sum(elem) for elem in zip(*pred))
        logging.info('Formatting report template')
        text = template.format(
            num_observations,
            heads, tails,
            heads_prob, tails_prob,
            num_steps,
            heads_pred, tails_pred
            )
        logging.info('Saving report to a file')
        reader.calc.save_file(text, output_file)
        logging.info('Sending message to Slack')
        reader.send_message_to_slack(success_message, webhook_url=webhook_url)
    except ValueError:
        reader.send_message_to_slack(failure_message, webhook_url=webhook_url)


if __name__ == '__main__':
    logging.basicConfig(
        format=logging_format,
        level=logging.NOTSET,
        handlers=[logging.FileHandler(log_file)]
        )
    main()
