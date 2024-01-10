from setuptools import setup, find_packages

setup(
    name="hypertraps",
    version="1.0",
    packages=find_packages(),
    scripts=[
        "scripts/run_convert_data_to_transitions.sh",
        "scripts/run_information_criterion.sh",
        "scripts/run_mcmc_sampler.sh",
        "scripts/run_plot_feature_graph.sh",
        "scripts/run_plot_hypercube_graph.sh",
        "scripts/run_plot_information_criterion.sh",
        "scripts/run_plot_mc_stats.sh",
        "scripts/run_plot_ordering_histograms.sh",
        "scripts/run_plot_raw_data.sh",
        "scripts/run_pw.sh",
        "scripts/run_pw_regularised.sh",
    ],
    entry_points={
        "console_scripts": [
            "hypertraps-convert-data-to-transitions=src.python.convert_data_to_transitions:main",
            # "hypertraps-plot-feature-graph=plot_feature_graph:main",
            # "hypertraps-plot-hypercube-graph=plot_hypercube_graph:main",
            # "hypertraps-plot-information-criterion=plot_information_criterion:main",
            # "hypertraps-plot-mc-stats=plot_mc_stats:main",
            # "hypertraps-plot-ordering-histogram=plot_ordering_histogram:main",
            # "hypertraps-plot-raw-data=plot_raw_data:main",
        ]
    }
)

