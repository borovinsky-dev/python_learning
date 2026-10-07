from threading import Thread


def create_massive(rows: int, colls: int):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(colls):
            row.append(0)
        matrix.append(row)


def fill_row(matrix: list[list[int]], row_index: int) -> None:
    for col_index in range(len(matrix[row_index])):
        matrix[row_index][col_index] = col_index


def main():
    rows = 5
    cols = 5

    matrix = create_massive(rows, cols)

    threads = []

    # Создаём отдельный поток для каждой строки
    for row_index in range(rows):
        thread = Thread(target=fill_row, args=(matrix, row_index))

        threads.append(thread)
        thread.start()

    # Ждём завершения всех потоков
    for thread in threads:
        thread.join()

    print(matrix)


main()
