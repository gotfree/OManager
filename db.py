import yaml
import pprint


pp = pprint.PrettyPrinter(indent=2)

with open("db_scheme.yml", "r") as stream:
    try:
        D = yaml.safe_load(stream)
        pp.pprint(D)
    except yaml.YAMLError as exc:
        print(exc)
