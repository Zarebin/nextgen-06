from Modules import unicode_convertor, html_parser, tokenizer, tf_idf_calc
import os

base_path = "D:\\Downloads\\Compressed\\project-dp-trend-description\\csv\\"

csv_files = os.listdir(base_path)

for file in csv_files:
    file_name = file

    html = unicode_convertor.get_clear(base_path + file_name)
    tags = html_parser.main_content_finder(html)
    tokenized_contents = tokenizer.tokenize_contents(tags)
    sentences = tokenized_contents[0]
    words = tokenized_contents[1][0]
    scores_per_words = tf_idf_calc.tf_idf(sentences, words)
    f = open(file_name+"words_scores.txt", "a", encoding="utf-8")
    f.write(f"Words scores in file {file} are equals with: {scores_per_words}")
    f.close()


