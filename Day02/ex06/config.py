filepath = 'data.csv'
num_steps = 3
template = """Report
We have made {} observations of tossing a coin: {} tails and {} heads.
The probabilities are {:.2f}% and {:.2f}% respectively.
Predictions for the next {} observations: {} tails and {} heads.
"""
output_file = 'report'
log_file = 'analytics.log'
logging_format = '%(asctime)-15s %(message)s'
webhook_url = None
success_message = 'The report has been successfully created'
failure_message = 'The report hasn’t been created due to an error'
