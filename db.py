import yaml
import pprint


pp = pprint.PrettyPrinter(indent=2)


def myprint(d):
  for k, v in d.items():
    if isinstance(v, dict):
      myprint(v)
    elif isinstance(v, list):
        # make key repr for items lists
        for i in v:
            print(f"{i}")
    else:
      pp.pprint(f"{k}")


with open("db_scheme.yml", "r") as stream:
    try:
        D = yaml.safe_load(stream)
        myprint(D)
    except yaml.YAMLError as exc:
        print(exc)
