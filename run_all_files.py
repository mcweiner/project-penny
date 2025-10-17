import src.yield_generator as yield_generator
import src.scorer as scorer
import src.score_all_combos as score_all_combos
import src.win_draw_heatmap_generator as heatmap
import runpy

# Main execution to run all components
if __name__ == "__main__":
    # Run the yield generator script
    runpy.run_path("src/yield_generator.py")
    
    # Run the score all combinations script
    runpy.run_path("src/score_all_combos.py")
    
    # Run the win/draw heatmap generator script
    runpy.run_path("src/win_draw_heatmap_generator.py")
