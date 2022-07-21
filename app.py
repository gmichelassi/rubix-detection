from rubik_detection import main as processing_main
from rubik_synthesis import main as synthesis_main


rubix_images = [
    'teste1.JPG',
    # 'teste2.JPG'
    # 'front.JPG',
    # 'bottom.JPG',
    # 'back.JPG',
    # 'top.JPG',
    # 'right.JPG',
    # 'left.JPG',
    # 'will_work.JPG',
    # 'wont_work_1.JPG',
    # 'wont_work_2.JPG'
]


if __name__ == '__main__':
    results = processing_main(rubix_images)

    print(results)
