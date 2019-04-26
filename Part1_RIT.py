
# TODO: parameterize this file for inputs VCF, output file name, and insert length
vcf_file = r"gnomad.exomes.r2.1.1.sites.21.vcf"
fastA = r"fastAchr21.fa"

import vcf

vcf_reader = vcf.Reader(open(vcf_file, 'r'))
record = next(vcf_reader)
i = 1

for record in vcf_reader:
    if (record.var_type != "snp") and (record.var_subtype == "ins"):
        alt_seq = record.ALT
        chrom = record.CHROM
        pos = record.POS
        alt_seq = str(alt_seq).replace('[', '').replace(']', '')
        alt_seq_length = len(alt_seq)
        if alt_seq_length > 25:
	    #if an insertion exists at the same then same chr and position then unique name
	    #subtract ref seq length from alt seq length and if that greater 25
            # TODO: keep track of whether an insertion at this site exists
            # and add to counter to make a unique fastA header
            text = (">chr" + str(chrom) + ":" + str(pos) + "_"  +  "\n" + alt_seq)
            # print(text)
            with open(fastA, 'a') as fasta:
                fasta.write(text + '\n')
            i = i + 1

print("done")
