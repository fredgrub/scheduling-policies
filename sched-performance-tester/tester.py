import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add arguments to the parser
    parser.add_argument("--queue", type=int, default=32, help="Queue set size")
    parser.add_argument("--state", type=int, default=16, help="State set size")
    parser.add_argument("--experiments",
                        choices=["actual", "estimated", "backfilling"],
                        default=["actual", "estimated", "backfilling"],
                        nargs="+",
                        help="Experiments configuration")
    parser.add_argument("--traces",
                        choices=["ANL", "CURIE", "CTC-SP2", "HPC2N", "SDSC-BLUE", "SDSC-SP2", "L256", "L256e", "L1024", "L1024e"],
                        default=["L256"],
                        nargs="+",
                        help="Platform traces")

    # Parse the arguments
    args = parser.parse_args()

    print(f"Queue size: {args.queue:d}\nState size: {args.state:d}")
    print(f"Experiments: {args.experiments}")
    print(f"Platforms: {args.traces}")


if __name__ == "__main__":
    main()
