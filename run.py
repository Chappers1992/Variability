import yaml
import argparse
from jinja2 import Environment, FileSystemLoader, Template

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--jobs',
                        required=True)
    parser.add_argument('--job_config',
                        required=True)

    return parser.parse_args()

def get_commandline(args):
    config_data = yaml.load(open(args.job_config))
    job_data = config_data[args.jobs]
    env = Environment(loader=FileSystemLoader('Templates'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(args.jobs)

    return template.render(job_data)

def main():
    args = get_args()
    commandline = get_commandline(args)
    print(commandline)

if __name__ == '__main__':
    main()