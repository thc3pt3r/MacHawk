import sigma
import sigma.backends


def evaluate_sigma_rule(rulepath, logname):
    sigma_rule = sigma.load(rulepath)

    with open(logname, 'r') as log_file:
        log_data = log_file.read()

    backend = sigma.backends.ConditionBackend()

    matches = list(backend.match(sigma_rule, log_data))

    return matches