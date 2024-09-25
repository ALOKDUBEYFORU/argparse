
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Sample program")
    parser.add_argument('number1',help="enter number1")
    parser.add_argument("number2",help="enter number2")
    parser.add_argument("operation",help='Enter operation')
    args = parser.parse_args()
    result = None
    args.number1 = int(args.number1)
    args.number2 = int(args.number2)

    if args.operation == 'add':
        result = args.number1+args.number2
    elif args.operation == 'multiply':
        result = args.number1+args.number2
    elif args.operation == 'division':
        result = args.number1/args.number2
    else:
        print("Invalid operation")
    print('First Number',args.number1)
    print('Second Number',args.number2)
    print("Operations",args.operation)
    print('Result :',result)
