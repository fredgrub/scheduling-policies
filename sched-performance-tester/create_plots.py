import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# actual_file = "experiments/SDSC_BLUE_runtimes.csv"
# estimated_file = "experiments/SDSC_BLUE_estimate.csv"
# plot_file = "SDSC_BLUE_boxplots.pdf"

# actual_df = pd.read_csv(actual_file, usecols=["FCFS","WFP3","UNICEF","SPT","SAF","F2","LIN"]).assign(Scenario="Actual")
# estimated_df = pd.read_csv(estimated_file, usecols=["FCFS","WFP3","UNICEF","SPT","SAF","F2","LIN"]).assign(Scenario="Estimated")

# # print(actual_df.Location)

# cdf = pd.concat([actual_df, estimated_df])    
# mdf = pd.melt(cdf, id_vars=['Scenario'], var_name=['Scheduling policies'])

# mdf.rename(columns={'value':'Average bounded slowdown'}, inplace=True)

# # print(mdf.head())

# ax = sns.boxplot(x="Scheduling policies", y="Average bounded slowdown", hue="Scenario", data=mdf, linewidth=0.5, palette="Pastel1", fliersize=0)
# sns.stripplot(x='Scheduling policies', y='Average bounded slowdown', hue='Scenario', data=mdf, jitter=True, dodge=True, palette="Pastel1", linewidth=0.5, size=3)

# # Get the handles and labels. For this example it'll be 2 tuples
# # of length 4 each.
# handles, labels = ax.get_legend_handles_labels()

# # When creating the legend, only use the first two elements
# # to effectively remove the last two.
# l = plt.legend(handles[0:2], labels[0:2])

# plt.savefig(plot_file, dpi=400)

#### Single boxplot

data = pd.read_csv("experiments/SDSC_BLUE_runtimes.csv", usecols=["FCFS","WFP3","UNICEF","SPT","SAF","F2","LIN"])
plottable_data = pd.melt(data)

plottable_data.rename(columns={'variable': 'Scheduling policies','value':'Average bounded slowdown'}, inplace=True)

ax = sns.boxplot(x="Scheduling policies", y="Average bounded slowdown", data=plottable_data, linewidth=0.5, palette="Pastel1", fliersize=0)
sns.stripplot(x="Scheduling policies", y="Average bounded slowdown", data=plottable_data, jitter=True, dodge=True, palette="Pastel1", linewidth=0.5, size=3)

#handles, labels = ax.get_legend_handles_labels()
#l = plt.legend(handles[0:2], labels[0:2])

plt.savefig("SDSC_BLUE_runtimes_boxplot.pdf", dpi=400)

