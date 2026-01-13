import json
import argparse



def main():
    parser = argparse.ArgumentParser(description='Convert Minecraft advancement files into triggers for lockout goals.')
    parser.add_argument('file', nargs='*')

    args = parser.parse_args()

    for file in args.file:

        with open(file, 'r') as f:
            advancement = json.load(f)

        if 'display' in advancement:
            advancement.pop('display')
        if 'parent' in advancement:
            advancement.pop('parent')
        advancement['rewards'] = {"function": "lockout:goals/count/advancements"}

        with open(file, 'w') as f:
            json.dump(advancement, f, indent=4)

        print('Success!')

        

if __name__ == '__main__':
    main()

