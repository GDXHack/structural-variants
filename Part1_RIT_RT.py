## AUTHORS


# TODO: parameterize this file for inputs VCF, output file name, and insert length, and chrom
vcf_file = "/mnt/hnas/bioinfo/projects/VariantInfoDownloads/ExAC/gnomAD/Version2.1/genomes/gnomad.genomes.r2.1.sites.vcf.gz"
fastA = "fastAchr21.fa"

import vcf

vcf_reader = vcf.Reader(open(vcf_file, 'r'))
# vcf_reader = vcf.Reader(filename=vcf_file)
record = next(vcf_reader)
all_pos = {}
for record in vcf_reader.fetch('21'):
# for record in vcf_reader:
    if (record.var_type != "snp") and (record.var_subtype == "ins"):
        alt_seq = record.ALT
        ref_seq = record.REF
        chrom = record.CHROM
        pos = record.POS
        ref_seq = str(ref_seq).replace('[', '').replace(']', '')
        alt_seq = str(alt_seq).replace('[', '').replace(']', '')
        alt_seq_length = len(alt_seq) - len(ref_seq)
        if alt_seq_length > 25:
            pos = (">chr" + str(chrom) + ":" + str(pos))
            if pos in all_pos:
                all_pos[pos]+=1
            else:
                all_pos[pos]=1
            text = (">chr" + str(chrom) + ":" + str(pos) + "_"  + all_pos[pos] +  "\n" + alt_seq)
            # print(text)
            with open(fastA, 'a') as fasta:
                fasta.write(text + '\n')
                break
            break


print("done")
