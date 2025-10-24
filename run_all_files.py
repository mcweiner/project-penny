import runpy
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# Main execution to run all components
if __name__ == "__main__":
    generate_question = input("Do you want recreate our results (y/n): ").strip().lower()
    if generate_question == 'y':
        # Run the yield generator script
        runpy.run_module("src.yield_generator", run_name="__main__")

        # Run the score all combinations script
        runpy.run_module("src.score_all_combos", run_name="__main__")

        # Run the win/draw heatmap generator script
        runpy.run_module("src.win_draw_heatmap_generator", run_name="__main__")
    else:
        runpy.run_module("src.win_draw_heatmap_generator", run_name="__main__")