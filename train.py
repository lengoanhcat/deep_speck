import train_nets as tn
import argparse


def main():
    parser = argparse.ArgumentParser(description='Train Neural Disguisher')
    parser.add_argument('--epochs', type=int, help='number of epochs')
    parser.add_argument('--rounds', type=int, help='number of encryption rounds')
    parser.add_argument('--layers', type=int, help='number of resnet layers')
    parser.add_argument('--datagen', type=str, help='mode of data generation')

    args = parser.parse_args()

    tn.train_speck_distinguisher(
        args.epochs,num_rounds=args.rounds,
        depth=args.layers,datagen=args.datagen);

if __name__ == "__main__":
    # execute only if run as script
    main()
