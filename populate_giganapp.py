import os
import django


def populate():
    soapdvo2_paper = add_paper(doi_suffix='2047-217X-1-18',
                               gigasci_url='http://www.gigasciencejournal.com/content/1/1/18',
                               title='SOAPdenovo2: an empirically improved memory-efficient short-read de novo assembler',
                               authors='Ruibang Luo, Binghang Liu, Yinlong Xie, Zhenyu Li, Weihua Huang, Jianying Yuan, Guangzhu He, Yanxiang Chen, Qi Pan, Yunjie Liu, Jingbo Tang, Gengxiong Wu, Hao Zhang, Yujian Shi, Yong Liu, Chang Yu, Bo Wang, Yao Lu, Changlei Han, David W Cheung, Siu-Ming Yiu, Shaoliang Peng, Zhu Xiaoqian, Guangming Liu, Xiangke Liao, Yingrui Li, Huanming Yang, Jian Wang, Tak-Wah Lam and Jun Wang',
                               article_type='RA',
                               shortname='Soapdenovo2',
                               journal='GigaScience',
                               year='2012',
                               volume='1',
                               page='18',
                               image_url='/static/images/dna.png',
                               background='There is a rapidly increasing amount of de novo genome assembly using next-generation sequencing (NGS) short reads; however, several big challenges remain to be overcome in order for this to be efficient and accurate. SOAPdenovo has been successfully applied to assemble many published genomes, but it still needs improvement in continuity, accuracy and coverage, especially in repeat regions.',
                               results='To overcome these challenges, we have developed its successor, SOAPdenovo2, which has the advantage of a new algorithm design that reduces memory consumption in graph construction, resolves more repeat regions in contig assembly, increases coverage and length in scaffold construction, improves gap closing, and optimizes for large genome.',
                               conclusions='Benchmark using the Assemblathon1 and GAGE datasets showed that SOAPdenovo2 greatly surpasses its predecessor SOAPdenovo and is competitive to other assemblers on both assembly length and accuracy. We also provide an updated assembly version of the 2008 Asian (YH) genome using SOAPdenovo2. Here, the contig and scaffold N50 of the YH genome were ~20.9 kbp and ~22 Mbp, respectively, which is 3-fold and 50-fold longer than the first published version. The genome coverage increased from 81.16% to 93.91%, and memory consumption was ~2/3 lower during the point of largest memory consumption.')

    soapdvo2_fig1 = add_figure(paper=soapdvo2_paper,
                               title="Figure 1. A comparison of the scaffold N10 to N90 between the assemblies based on the Assemblathon 1 dataset.",
                               url="http://www.gigasciencejournal.com/content/1/1/18/figure/F1",
                               figure_num="1",
                               tbn_file="/static/images/2047-217X-1-18-1.gif")

    add_figure_workflow(paper=soapdvo2_paper,
                        figure=soapdvo2_fig1,
                        url="",
                        name="fig1_wf",
                        title="",
                        description="")

    soapdvo2_fig2 = add_figure(paper=soapdvo2_paper,
                               title="Figure 2. A comparison of the scaffold N10 to N90 between the assemblies based on the new YH sequencing data.",
                               url="http://www.gigasciencejournal.com/content/1/1/18/figure/F2",
                               figure_num="2",
                               tbn_file="/static/images/2047-217X-1-18-2.gif")

    add_figure_workflow(paper=soapdvo2_paper,
                        figure=soapdvo2_fig2,
                        url="",
                        name="fig2_wf",
                        title="",
                        description="")

    soapdvo2_tab1 = add_table(paper=soapdvo2_paper,
                              title="Table 1. Evaluation of Assemblathon1 dataset assemblies.",
                              url="http://www.gigasciencejournal.com/content/1/1/18/table/T1",
                              table_num="1",
                              tbn_file="/static/images/2047-217X-1-18-T1.png")

    add_table_workflow(paper=soapdvo2_paper,
                       table=soapdvo2_tab1,
                       url="",
                       name="tab1_wf",
                       title="",
                       description="")

    soapdvo2_tab2 = add_table(paper=soapdvo2_paper,
                              title="Table 2. Assemblies of S. aureus and R. sphaeroides.",
                              url="http://www.gigasciencejournal.com/content/1/1/18/table/T2",
                              table_num="2",
                              tbn_file="/static/images/2047-217X-1-18-T2.png")

    add_table_workflow(paper=soapdvo2_paper,
                       table=soapdvo2_tab2,
                       url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=a0d84b45643a2678",
                       name="tab2_wf1",
                       title="SOAPdenovo2 assembly of S. aureus short reads",
                       description="This pipeline uses SOAPdenovo2 to assemble short reads from S. aureus. Statistics for the assembly are calculated using the GAGE analysis script")

    add_table_workflow(paper=soapdvo2_paper,
                       table=soapdvo2_tab2,
                       url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=b23533e4ff1bb7ec",
                       name="tab2_wf2",
                       title="SOAPdenovo2 assembly of R. sphaeroides short reads",
                       description="This pipeline uses SOAPdenovo2 to assemble short reads from R. sphaeroides. Statistics for the assembly are calculated using the GAGE analysis script")

    add_table_workflow(paper=soapdvo2_paper,
                       table=soapdvo2_tab2,
                       url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=b23533e4ff1bb7ec",
                       name="tab2_wf3",
                       title="SOAPdenovo1 assembly of S. aureus short reads",
                       description="This pipeline uses SOAPdenovo2 to assemble short reads from S. aureus. Statistics for the assembly are calculated using the GAGE analysis script")

    add_table_workflow(paper=soapdvo2_paper,
                       table=soapdvo2_tab2,
                       url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=33c1d4ca9f8bc33c",
                       name="tab2_wf4",
                       title="SOAPdenovo1 assembly of R. sphaeroides short reads",
                       description="This pipeline uses SOAPdenovo1 to assemble short reads from S. aureus. Statistics for the assembly are calculated using the GAGE analysis script")

    add_table_workflow(paper=soapdvo2_paper,
                       table=soapdvo2_tab2,
                       url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=40876639881ca029",
                       name="tab2_wf5",
                       title="ALL-PATHS assembly of S. aureus short reads",
                       description="This pipeline uses ALL-PATHS to assemble short reads from S. aureus. Statistics for the assembly are calculated using the GAGE analysis script")

    add_table_workflow(paper=soapdvo2_paper,
                       table=soapdvo2_tab2,
                       url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=d071e794759ab192",
                       name="tab2_wf6",
                       title="ALL-PATHS assembly of R. sphaeroides short reads",
                       description="This pipeline uses ALL-PATHS to assemble short reads from R. sphaeroides. Statistics for the assembly are calculated using the GAGE analysis script")

    soapdvo2_tab3 = add_table(paper=soapdvo2_paper,
                              title="Table 3. Assemblies of Bombus Impatiens.",
                              url="http://www.gigasciencejournal.com/content/1/1/18/table/T3",
                              table_num="3",
                              tbn_file="/static/images/2047-217X-1-18-T3.png")

    add_table_workflow(paper=soapdvo2_paper,
                       table=soapdvo2_tab3,
                       url="",
                       name="tab3_wf",
                       title="",
                       description="")

    goo_paper = add_paper(doi_suffix='2047-217X-2-4',
                          gigasci_url='http://www.gigasciencejournal.com/content/2/1/4',
                          title='Ultra-deep sequencing enables high-fidelity recovery of biodiversity for bulk arthropod samples without PCR amplification',
                          authors='Xin Zhou, Yiyuan Li, Shanlin Liu, Qing Yang, Xu Su, Lili Zhou, Min Tang, Ribei Fu, Jiguang Li and Quanfei Huang',
                          article_type='RA',
                          shortname='Squishome',
                          journal='GigaScience',
                          year='2013',
                          volume='2',
                          page='4',
                          image_url='/static/images/dna.png',
                          background='Next-generation-sequencing (NGS) technologies combined with a classic DNA barcoding approach have enabled fast and credible measurement for biodiversity of mixed environmental samples. However, the PCR amplification involved in nearly all existing NGS protocols inevitably introduces taxonomic biases. In the present study, we developed new Illumina pipelines without PCR amplifications to analyze terrestrial arthropod communities.',
                          results='Mitochondrial enrichment directly followed by Illumina shotgun sequencing, at an ultra-high sequence volume, enabled the recovery of Cytochrome c Oxidase subunit 1 (COI) barcode sequences, which allowed for the estimation of species composition at high fidelity for a terrestrial insect community. With 15.5 Gbp Illumina data, approximately 97% and 92% were detected out of the 37 input Operational Taxonomic Units (OTUs), whether the reference barcode library was used or not, respectively, while only 1 novel OTU was found for the latter. Additionally, relatively strong correlation between the sequencing volume and the total biomass was observed for species from the bulk sample, suggesting a potential solution to reveal relative abundance.',
                          conclusions='The ability of the new Illumina PCR-free pipeline for DNA metabarcoding to detect small arthropod specimens and its tendency to avoid most, if not all, false positives suggests its great potential in biodiversity-related surveillance, such as in biomonitoring programs. However, further improvement for mitochondrial enrichment is likely needed for the application of the new pipeline in analyzing arthropod communities at higher diversity.')

    goo_fig1 = add_figure(paper=goo_paper,
                          title="Figure 1. Schematic pipelines of conventional and PCR-independent NGS biodiversity analyses.",
                          url="http://www.gigasciencejournal.com/content/2/1/4/figure/F1",
                          figure_num="1",
                          tbn_file="/static/images/2047-217X-2-4-1.gif")

    add_figure_workflow(paper=goo_paper,
                        figure=goo_fig1,
                        url="",
                        name="fig1_wf",
                        title="",
                        description="")

    goo_fig2 = add_figure(paper=goo_paper,
                          title="Figure 2. Assembly results of mitochondrial genes.",
                          url="http://www.gigasciencejournal.com/content/2/1/4/figure/F2",
                          figure_num="2",
                          tbn_file="/static/images/2047-217X-2-4-2.gif")

    add_figure_workflow(paper=goo_paper,
                        figure=goo_fig2,
                        url="",
                        name="fig2_wf",
                        title="",
                        description="")

    goo_fig3 = add_figure(paper=goo_paper,
                          title="Figure 3. Rarefaction curves for discoveries of (A) MOTUs and (B) biomass.",
                          url="http://www.gigasciencejournal.com/content/2/1/4/figure/F3",
                          figure_num="3",
                          tbn_file="/static/images/2047-217X-2-4-3.gif")

    add_figure_workflow(paper=goo_paper,
                        figure=goo_fig3,
                        url="",
                        name="fig3_wf",
                        title="",
                        description="")

    goo_fig4 = add_figure(paper=goo_paper,
                          title="Figure 4. Correlation between biomass and data volume.",
                          url="http://www.gigasciencejournal.com/content/2/1/4/figure/F4",
                          figure_num="4",
                          tbn_file="/static/images/2047-217X-2-4-4.gif")

    add_figure_workflow(paper=goo_paper,
                        figure=goo_fig4,
                        url="",
                        name="fig4_wf",
                        title="",
                        description="")

    goo_tab1 = add_table(paper=goo_paper,
                         title="Table 1. Sample composition, sequencing information and COI recovery rates of the bulk insect sample.",
                         url="http://www.gigasciencejournal.com/content/2/1/4/table/T1",
                         table_num="1",
                         tbn_file="/static/images/2047-217X-2-4-T1.png")

    add_table_workflow(paper=goo_paper,
                       table=goo_tab1,
                       url="",
                       name="tab1_wf",
                       title="",
                       description="")

    goo_tab2 = add_table(paper=goo_paper,
                         title="Table 2. Results of de novo assembly for the 35 detected COI scaffolds and 370 mitochondrial scaffolds.",
                         url="http://www.gigasciencejournal.com/content/2/1/4/table/T2",
                         table_num="2",
                         tbn_file="/static/images/2047-217X-2-4-T2.png")

    add_table_workflow(paper=goo_paper,
                       table=goo_tab2,
                       url="",
                       name="tab2_wf",
                       title="",
                       description="")

    gendiv_paper = add_paper(doi_suffix='2047-217X-2-17',
                             gigasci_url='http://www.gigasciencejournal.com/content/2/1/17',
                             title='Galaxy tools to study genome diversity',
                             authors='Oscar C Bedoya-Reina, Aakrosh Ratan, Richard Burhans, Hie Lim Kim, Belinda Giardine, Cathy Riemer, Qunhua Li, Thomas L Olson, Thomas P Loughran, Bridgett M vonHoldt, George H Perry, Stephan C Schuster and Webb Miller',
                             article_type='RA',
                             shortname='genomicdiv',
                             journal='GigaScience',
                             year='2013',
                             volume='2',
                             page='17',
                             image_url='/static/images/dna.png',
                             background='Intra-species genetic variation can be used to investigate population structure, selection, and gene flow in non-model vertebrates; and due to the plummeting costs for genome sequencing, it is now possible for small labs to obtain full-genome variation data from their species of interest. However, those labs may not have easy access to, and familiarity with, computational tools to analyze those data.',
                             results='We have created a suite of tools for the Galaxy web server aimed at handling nucleotide and amino-acid polymorphisms discovered by full-genome sequencing of several individuals of the same species, or using a SNP genotyping microarray. In addition to providing user-friendly tools, a main goal is to make published analyses reproducible. While most of the examples discussed in this paper deal with nuclear-genome diversity in non-human vertebrates, we also illustrate the application of the tools to fungal genomes, human biomedical data, and mitochondrial sequences.',
                             conclusions='This project illustrates that a small group can design, implement, test, document, and distribute a Galaxy tool collection to meet the needs of a particular community of biologists.')

    gendiv_fig1 = add_figure(paper=gendiv_paper,
                             title="Figure 1. Specifying a population.",
                             url="http://www.gigasciencejournal.com/content/2/1/17/figure/F1",
                             figure_num="1",
                             tbn_file="/static/images/2047-217X-2-17-1.gif")

    add_figure_workflow(paper=gendiv_paper,
                        figure=gendiv_fig1,
                        url="",
                        name="fig1_wf",
                        title="",
                        description="")

    gendiv_fig2 = add_figure(paper=gendiv_paper,
                             title="Figure 2. Commands for the aye-aye example.",
                             url="http://www.gigasciencejournal.com/content/2/1/17/figure/F2",
                             figure_num="2",
                             tbn_file="/static/images/2047-217X-2-17-2.gif")

    add_figure_workflow(paper=gendiv_paper,
                        figure=gendiv_fig2,
                        url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=f7bb1edd6b95db62",
                        name="fig2_wf1",
                        title="Genetic diversity and structure of Aye-Aye populations",
                        description="Three populations of Aye-Aye lemurs from Madagasgar were examined for their genetic diversity by analysing their SNP data using phylogenetic tree, principle components analysis and population structure analysis tools.")

    add_figure_workflow(paper=gendiv_paper,
                        figure=gendiv_fig2,
                        url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=b887d74393f85b6d",
                        name="fig2_wf2",
                        title="Diversity of Aye-Aye populations using the Fixation index",
                        description="The fixation index was calculated from Aye-aye lemur SNP data to assess the level of genetic variation in the three populations.")

    add_figure_workflow(paper=gendiv_paper,
                        figure=gendiv_fig2,
                        url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=f0f309c56aff0025",
                        name="fig2_wf3",
                        title="Nucleotide diversity of Aye-Aye populations",
                        description="The degree of polymorphism within a population can be measured by examining nucleotide diversity. One measure of nucleotide diversity is pi, the average number of nucleotide differences per site between any two DNA sequences chosen randomly from the sample population. pi was evaluated in this workflow by synthesizing a human data set that matched the Aye-aye sequences in numbers of individuals and sequence depth. The results shown in the history suggest that nucleotide diversity within each of the three Aye-aye populations is relatively low.")

    add_figure_workflow(paper=gendiv_paper,
                        figure=gendiv_fig2,
                        url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=f0f309c56aff0025",
                        name="fig2_wf4",
                        title="Amino acid diversity of aye-aye populations",
                        description="The results shown in the history contains tabular data of putative amino-acid polymorphisms from the Aye-aye populations. This result was produced by mapping assembled contigs from the Aye-aye and the SNPs they possess to the human genome. Human gene annotations were then used to infer coding exons in the Aye-aye. The results of this analysis have not been published, and so the observations presented here are used to illustrate the use of additional Galaxy tools from the genome diversity tool set.")



    gendiv_fig3 = add_figure(paper=gendiv_paper,
                             title="Figure 3. Two KEGG pathways from the aye-aye data.",
                             url="http://www.gigasciencejournal.com/content/2/1/17/figure/F3",
                             figure_num="3",
                             tbn_file="/static/images/2047-217X-2-17-3.gif")

    add_figure_workflow(paper=gendiv_paper,
                        figure=gendiv_fig3,
                        url="",
                        name="fig3_wf",
                        title="",
                        description="")

    gendiv_fig4 = add_figure(paper=gendiv_paper,
                             title="Figure 4. Commands for the chicken example.",
                             url="http://www.gigasciencejournal.com/content/2/1/17/figure/F4",
                             figure_num="4",
                             tbn_file="/static/images/2047-217X-2-17-4.gif")

    add_figure_workflow(paper=gendiv_paper,
                        figure=gendiv_fig4,
                        url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=42a2c611109e5ed3",
                        name="fig4_wf",
                        title="Detecting low heterozygosity regions in domestic breeds of chicken",
                        description="This workflow demonstrates a windows-free method for detecting regions of low heterozygosity in various combinations of domestic breeds of chicken to identify genomic regions associated with economically important traits, such as egg or meat production.")

    gendiv_fig5 = add_figure(paper=gendiv_paper,
                             title="Figure 5. Principal components analysis of canid data.",
                             url="http://www.gigasciencejournal.com/content/2/1/17/figure/F5",
                             figure_num="5",
                             tbn_file="/static/images/2047-217X-2-17-5.gif")

    add_figure_workflow(paper=gendiv_paper,
                        figure=gendiv_fig5,
                        url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=5a9381f02a7b89af",
                        name="fig5_wf",
                        title="Admixed ancestry of North American wolves and coyotes",
                        description="The demographic history and relationships between lineages of North American Canidae has often been studied using a handful of genetic markers with limited resolution of evolutionary relationships. A few dozen co-dominant or uniparentally-inherited markers will only provide a fraction of the evolutionary history. One of the main and long-debated topics of North American canids has been the degree of admixture and species ancestries. To address admixture among canids and better resolve their ancestry, a published study analyzed genotypes from 48,036 SNVs (hereafter, referred to as 48K) distributed genome-wide. In order to test the robustness of the Genome Diversity set of tools, the same dataset was re-analyzed in this workflow for admixed ancestry across wolves and coyotes of North America.")

    gendiv_fig6 = add_figure(paper=gendiv_paper,
                             title="Figure 6. Inadequately covered parts of colugo mitochondrial sequences.",
                             url="http://www.gigasciencejournal.com/content/2/1/17/figure/F6",
                             figure_num="6",
                             tbn_file="/static/images/2047-217X-2-17-6.gif")

    add_figure_workflow(paper=gendiv_paper,
                        figure=gendiv_fig6,
                        url="",
                        name="fig6_wf",
                        title="",
                        description="")

    gendiv_fig7 = add_figure(paper=gendiv_paper,
                             title="Figure 7. Variants identified in cave-bear mitochondrial sequences.",
                             url="http://www.gigasciencejournal.com/content/2/1/17/figure/F7",
                             figure_num="7",
                             tbn_file="/static/images/2047-217X-2-17-7.gif")

    add_figure_workflow(paper=gendiv_paper,
                        figure=gendiv_fig7,
                        url="",
                        name="fig7_wf",
                        title="",
                        description="")

    gendiv_tab1 = add_table(paper=gendiv_paper,
                            title="Table 1. Examples discussed in this paper.",
                            url="http://www.gigasciencejournal.com/content/2/1/17/table/T1",
                            table_num="1",
                            tbn_file="/static/images/2047-217X-2-17-T1.png")

    add_table_workflow(paper=gendiv_paper,
                       table=gendiv_tab1,
                       url="",
                       name="tab1_wf",
                       title="",
                       description="")

    smilefinder_paper = add_paper(doi_suffix='2047-217X-X-XX',
                                  gigasci_url='',
                                  title='SmileFinder: a resampling-based approach to evaluate signatures of selection from genome-wide sets of matching allele frequency data in two or more diploid populations',
                                  authors="Wilfried M. Guiblet, Kai Zhao, Stephen J O'Brien, Steven E. Massey, Alfred L. Roca and Taras K. Oleksyk",
                                  article_type='TN',
                                  shortname='Smilefinder',
                                  journal='GigaScience',
                                  year='2015',
                                  volume='X',
                                  page='XX',
                                  image_url='/static/images/dna.png',
                                  background='Adaptive alleles may rise in frequency as a consequence of positive selection, creating a pattern of decreased variation in the neighboring loci, known as a selective sweep.  When the region containing this pattern is compared to another population with no history of selection, a rise in variance of allele frequencies between populations is observed. One challenge presented by large genome-wide datasets is the ability to differentiate between patterns that are remnants of natural selection from those expected to arise at random and/or as a consequence of selectively neutral demographic forces acting in the population.',
                                  results='SmileFinder is a simple program that looks for diversity and divergence patterns consistent with selection sweeps by evaluating allele frequencies in windows, including neighboring loci from two or more populations of a diploid species against the genome-wide neutral expectation. The program calculates the mean of heterozygosity and FST in a set of sliding windows of incrementally increasing sizes, and then builds a resampled distribution (the baseline) of random multi-locus sets matched to the sizes of sliding windows, using an unrestricted sampling. Percentiles of the values in the sliding windows are derived from the superimposed resampled distribution. The resampling can easily be scaled from 1K to 100M; the higher the number, the more precise the percentiles ascribed to the extreme observed values.   ',
                                  conclusions='The output from SmileFinder can be used to plot percentile values to look for population diversity and divergence patterns that may suggest past actions of positive selection along chromosome maps, and to compare lists of suspected candidate genes under random gene sets to test for the overrepresentation of these patterns among gene categories.  Both applications of the algorithm have already been used in published studies.  Here we present a publicly available, open source program that will serve as a useful tool for preliminary scans of selection using worldwide databases of human genetic variation, as well as population datasets for many non-human species, from which such data is rapidly emerging with the advent of new genotyping and sequencing technologies.')

    sf_fig1 = add_figure(paper=smilefinder_paper,
                         title="Figure 1. Description of the SmileFinder algorithm.",
                         url="",
                         figure_num="1",
                         tbn_file="/static/images/CUL5.png")

    add_figure_workflow(paper=smilefinder_paper,
                        figure=sf_fig1,
                        url="http://galaxy.cbiit.cuhk.edu.hk/workflow/export_to_file?id=319886f37b7797fe",
                        name="fig1_wf",
                        title="The diversity of two African populations",
                        description="SmileFinder is a tool for detects diversity and divergence patterns associated with selection sweeps by evaluating allele frequencies. The documentation on this page shows how the collection of SmileFinder scripts (which have been deployed as tools in GigaGalaxy) can be used within a workflow to identify a difference in diversity between two African populations.")

    # Print out what we have added to the user.
    for p in Paper.objects.all():
        for f in Figure.objects.filter(paper=p):
            print "- {0} - {1}".format(str(p), str(f))
    return p


def add_paper(doi_suffix, gigasci_url, title, authors, article_type, shortname, journal, year, volume, page, image_url,
              background, results, conclusions):
    p = Paper.objects.get_or_create(doi_suffix=doi_suffix,
                                    gigasci_url=gigasci_url,
                                    title=title,
                                    authors=authors,
                                    article_type=article_type,
                                    short_name=shortname,
                                    journal=journal,
                                    year=year,
                                    volume=volume,
                                    page=page,
                                    image_url=image_url,
                                    background=background,
                                    results=results,
                                    conclusions=conclusions)[0]
    return p


def add_figure(paper, title, url, tbn_file, figure_num):
    f = Figure.objects.get_or_create(paper=paper,
                                     title=title,
                                     url=url,
                                     tbn_file=tbn_file,
                                     figure_num=figure_num)[0]
    return f


def add_table(paper, title, url, tbn_file, table_num):
    t = Table.objects.get_or_create(paper=paper,
                                    title=title,
                                    url=url,
                                    tbn_file=tbn_file,
                                    table_num=table_num)[0]
    return t


def add_figure_workflow(paper, figure, url, name, title, description):
    wf = Workflow.objects.get_or_create(paper=paper,
                                        figure=figure,
                                        url=url,
                                        name=name,
                                        title=title,
                                        description=description)[0]
    return wf


def add_table_workflow(paper, table, url, name, title, description):
    wf = Workflow.objects.get_or_create(paper=paper,
                                        url=url,
                                        table=table,
                                        name=name,
                                        title=title,
                                        description=description)[0]
    return wf


# Start execution here!
if __name__ == '__main__':
    print "Starting GigaNapp population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aws-project.settings')
    from giganapp.models import Paper, Figure, Table, Workflow

    django.setup()
    populate()