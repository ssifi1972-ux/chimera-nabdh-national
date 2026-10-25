# CHIMERA ENGINE - FINAL VERSION - 25-10-2026
# Drone: 0.9x0.7x0.6m - 32kg - 5m safety - 40m trees - 25 sqm per ball

class FireBall:
    """5kg ball with explosive dispersal - 40m trees blocking"""
    def __init__(self):
        self.weight_kg = 5
        self.base_sqm = 10  # without explosion
        self.explosive_sqm = 35  # with explosion
        self.tree_blocking = 0.30  # 30% blocked by 40m trees
        self.real_sqm = 25  # FINAL: 25 sqm per ball with trees
        self.blast_radius = 3.5  # meters
        self.explosion_height = 2  # meters above ground

class Octocopter:
    """Real dimensions - Batna researcher"""
    def __init__(self, drone_id):
        self.id = drone_id
        self.length = 0.9  # m
        self.width = 0.7  # m
        self.height = 0.6  # m
        self.empty_weight = 12  # kg
        self.payload = 20  # kg
        self.balls = 4
        self.total_weight = 32  # kg
        self.sqm_per_drone = 100  # 4 balls x 25 sqm

class TriangleFlying:
    """Triangle formation - 2.5m to 5m safety spacing"""
    def __init__(self, spacing=5.0):
        self.drones = 10
        self.spacing = spacing  # 2.5m to 5m - safety
        self.balls_total = 40
        self.sqm_total = 1000  # 40 x 25 sqm
        self.base_width_2_5 = 10.3  # m with 2.5m spacing
        self.base_width_5 = 20.6  # m with 5m spacing
        self.coverage_type = "Carpet Extinguishing - Sjad"
        
    def get_stats(self):
        width = self.base_width_5 if self.spacing >= 5 else self.base_width_2_5
        return f"Triangle {self.drones} drones - {self.spacing}m spacing - {width}m wide - {self.sqm_total} sqm in 15s - {self.coverage_type}"

class ChimeraNational:
    """40 Wilayas - 4.1M Ha - Final"""
    def __init__(self):
        self.tree_height = 40  # m avg
        self.drone_altitude = 50  # m - 10m above trees
        self.fall_height = 48  # m
        self.fall_time = 3.13  # sec
        self.khenchela_drones = 50
        self.khenchela_sqm = 5000  # 0.5 Ha per wave
        self.national_drones = 1500
        self.national_sqm = 150000  # 15 Ha per wave
        self.towers = 150
        self.wilayas = 40
        
    def report(self):
        print("="*60)
        print("CHIMERA NATIONAL - FINAL - META HACKATHON 2026")
        print("="*60)
        print(f"Drone: 0.9x0.7x0.6m - 32kg - 4 balls x 5kg")
        print(f"Ball: 5kg = 25 sqm (40m trees + explosive blast 3.5m radius)")
        print(f"Tree height: {self.tree_height}m avg - Drone altitude: {self.drone_altitude}m")
        print(f"Fall: {self.fall_height}m in {self.fall_time}s - 110 km/h")
        print(f"Triangle 10 Drones (5m spacing): 1000 sqm in 15 sec - Carpet")
        print(f"Khenchela {self.khenchela_drones} drones: {self.khenchela_sqm} sqm = 0.5 Ha per wave")
        print(f"40 Wilayas {self.national_drones} drones: {self.national_sqm} sqm = 15 Ha per wave")
        print(f"Towers: {self.towers} - Solar + VHF/UHF + Black Box 1200°C")
        print(f"Camera: 1 x 360° Pas-a-Pas - 5-15km diameter")
        print("="*60)
        print("STATUS: READY FOR META GLOBAL HACKATHON - INDIE TRACK $150K")
        print("="*60)

# Run
if __name__ == "__main__":
    chimera = ChimeraNational()
    chimera.report()
    
    triangle_2_5 = TriangleFlying(spacing=2.5)
    triangle_5 = TriangleFlying(spacing=5.0)
    
    print(f"\n{triangle_2_5.get_stats()}")
    print(f"{triangle_5.get_stats()}")
    print(f"\nSafety: 2.5m to 5m spacing - Both cover >5m width - Carpet extinguishing")