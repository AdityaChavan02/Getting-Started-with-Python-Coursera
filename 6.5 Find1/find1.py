#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
#text = "X-DSPAM-Confidence:    0.8475";

text = "X-DSPAM-Confidence: 0.8475";
no = text.find(' ');
no1 = text.find('',no);
out=text[no+1:no1];
out=float(out);
print(out);
