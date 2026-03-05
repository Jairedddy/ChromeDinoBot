def get_game_state(page):

    return page.evaluate("""
    () => {
        const r = Runner.instance_;

        let obstacle = null;

        if (r.horizon.obstacles.length > 0){
            const o = r.horizon.obstacles[0];

            obstacle = {
                xPos: o.xPos,
                yPos: o.yPos,
                width: o.width,
                type: o.typeConfig.type
            };
        }

        return {
            score: r.distanceRan,
            speed: r.currentSpeed,
            trexX: r.tRex.xPos,
            obstacle: obstacle
        };
    }
    """)