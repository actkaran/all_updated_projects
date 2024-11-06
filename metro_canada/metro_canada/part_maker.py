def generate_parts(start, end, parts):
    # Calculate the number of IDs in each part
    ids_per_part = (end - start + 1) // parts
    remainder = (end - start + 1) % parts

    part_start = start
    for i in range(parts):
        part_end = part_start + ids_per_part - 1 + (1 if i < remainder else 0)
        yield part_start, part_end
        part_start = part_end + 1


if __name__ == '__main__':
    parts = 5
    spider = 'data'
    start = 0
    end = 25000

    for part_number, (part_start, part_end) in enumerate(generate_parts(start, end, parts), 1):
        print(f'start "{spider}_start_{part_start}_end_{part_end}" scrapy crawl {spider} -a start={part_start} -a end={part_end}')
