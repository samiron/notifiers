import sys
import os
import argparse
import traceback

parser = argparse.ArgumentParser(description='Updates you with latest GitHub repositories.')

parser.add_argument('-p, --profile', 
    type=str,
    help='Slack ')

args = parser.parse_args()

SELF_PATH = os.path.dirname(__file__)
CONFIG_DIR = SELF_PATH + '/config'
PROFILE_DIR = SELF_PATH + '/profiles'

def main():
    from notifiers.gsnotifier import GSNotifier
    #plx_random_hook_link = 'https://hooks.slack.com/services/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'
    seeka_int_hook_link = "https://hooks.slack.com/services/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"
    notifier = GSNotifier(seeka_int_hook_link)
    notifier.run()

if __name__ == '__main__':
    sys.path.append(os.path.join(SELF_PATH, "lib"))
    try:
        main()
    except Exception as err:
        traceback.print_exc()
