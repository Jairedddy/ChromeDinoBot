def get_game_state(page, score_divisor=10):
    """Get current game state. score_divisor converts distanceRan to displayed score (e.g. 10 for most clones)."""
    return page.evaluate(
        """
    (params) => {
        const r = Runner.instance_;
        const divisor = (params && params.scoreDivisor) || 10;

        let obstacle = null;

        if (r.horizon.obstacles.length > 0){
            const o = r.horizon.obstacles[0];
            const height = (o.height != null) ? o.height : 0;

            obstacle = {
                xPos: o.xPos,
                yPos: o.yPos,
                width: o.width,
                height: height,
                type: o.typeConfig.type
            };
        }

        // Displayed score: game shows ~floor(distanceRan/divisor); raw distanceRan is much larger
        const displayedScore = (r.distanceMeter && typeof r.distanceMeter.actualDistance === 'number')
            ? r.distanceMeter.actualDistance
            : Math.floor(r.distanceRan / divisor);

        return {
            score: displayedScore,
            speed: r.currentSpeed,
            trexX: r.tRex.xPos,
            obstacle: obstacle
        };
    }
    """,
        {"scoreDivisor": score_divisor},
    )