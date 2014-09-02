import collections


def get_file_name():
  file_name = raw_input("Enter file name: ")
  if not file_name: #Rene Fleschenberg's comment
    file_name = "mbox-short.txt"
  return file_name


def read_file(file_name):
  lines = []
  with open(file_name) as fh:
    for line in fh:
      lines.append(line)
  return lines


def get_find_from(lines):
  from_emails = []
  for line in lines:
    if line.startswith('From '):
      values = line.split()
      from_emails.append(values[1])
  return from_emails


def group_items_by_count(items):
  items_counts = collections.defaultdict(int)
  for item in items:
    items_counts[item] += 1
  return items_counts


def main():
  file_name = get_file_name()
  lines = read_file(file_name)
  from_emails = get_from_fileds(lines)
  emails_counts = group_items_by_count(from_emails)
  # http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value <3
  max_email = sorted(emails_counts.iteritems(), key=operator.itemgetter(1))[-1]
  print max_email[0] + " " + str(max_email[1])


if __name__ == "__main__":
   main()
