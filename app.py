import argparse

from rubik_detection import main as processing_main
from rubik_synthesis import main as synthesis_main


rubix_images = [
    'teste1.JPG',
    'teste2.JPG',
    'teste3.JPG',
    'teste4.JPG',
    'teste5.JPG',
    'teste6.JPG',
    'teste7.JPG',
    'teste8.JPG',
    'teste9.JPG',
    'teste10.JPG',
    'teste11.JPG',
    'teste12.JPG',
    'teste13.JPG',
    'teste14.JPG',
    'teste15.JPG',
    'teste16.JPG',
    'teste17.JPG',
    'teste18.JPG',
    'will_work.JPG',
    'wont_work_1.JPG',
    'wont_work_2.JPG'
]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--synthesis', type=bool, default=False)
    parser.add_argument('--processing', type=bool, default=False)
    parser.add_argument('--file', type=str, default=None)
    parser.add_argument('--show_results', type=bool, default=False)

    args = parser.parse_args()

    if args.synthesis:
        synthesis_main()
    elif args.processing:
        if args.file is not None:
            rubix_images.append(args.file)

        results = processing_main(rubix_images=rubix_images, show_results=args.show_results)

        print(results)
