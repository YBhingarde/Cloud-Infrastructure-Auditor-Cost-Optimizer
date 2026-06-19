import os
import json
import csv
import logging
from datetime import datetime
from typing import List, Dict, Any
# Importing Rich components for UI implementation
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Setup basic logging for Member 4 Module
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Initialize Rich Console
console = Console()

class ReportFormatter:
    """
    Day 3 Complete: Reporting & Formatting Engine (Member 4 Module).
    Transforms raw scanner contracts into Rich terminal tables and exports files.
    """
    
    @staticmethod
    def display_terminal_report(resources: List[Dict[str, Any]]):
        """
        Renders a high-grade FinOps dashboard in the terminal using Rich.
        """
        console.print("\n")
        # Beautiful Header Box
        console.print(Panel.fit(
            "[bold green]CLOUD INFRASTRUCTURE AUDITOR & COST OPTIMIZER[/bold green]\n"
            "[bold white]FinOps Actionable Cost-Saving Report (CLI Edition)[/bold white]",
            border_style="cyan"
        ))
        
        if not resources:
            console.print("[bold yellow]✔ No underutilized resources detected! Your infrastructure is optimized.[/bold yellow]\n")
            return

        # Initialize Rich Table with Custom Styling
        table = Table(title="Identified Zombie/Underutilized Resources", title_style="bold magenta", show_lines=True)
        
        table.add_column("Resource ID", style="cyan", no_wrap=True)
        table.add_column("Type", style="bold yellow")
        table.add_column("Region", style="white")
        table.add_column("Status", style="green")
        table.add_column("Avg CPU (%) / Metrics", style="magenta")
        table.add_column("Est. Wasted Cost (Monthly)", style="bold red", justify="right")

        total_monthly_waste = 0.0

        # Loop through data contract and populate rows
        for res in resources:
            metrics = res.get("metrics", {})
            avg_cpu = metrics.get("average_cpu", "N/A")
            cost = metrics.get("wasted_cost_usd", 0.0)
            total_monthly_waste += cost

            table.add_row(
                res["resource_id"],
                res["resource_type"],
                res["region"],
                res["status"],
                f"{avg_cpu}% (Window: {metrics.get('days_window', 14)}d)",
                f"${cost:.2f}"
            )

        # Print the populated table to terminal
        console.print(table)
        
        # Display Total Savings Box
        console.print(Panel.fit(
            f"[bold red]🚨 TOTAL POTENTIAL MONTHLY WASTED COST: ${total_monthly_waste:.2f}[/bold red]\n"
            f"[bold white]Action Required: Review cleanup commands to reclaim budget.[/bold white]",
            border_style="red"
        ))
        console.print("\n")

    @staticmethod
    def export_report(resources: List[Dict[str, Any]], format_type: str = "json", filename: str = "audit_report"):
        """
        Day 3 Final Feature: Saves the generated scan reports as CSV and JSON files
        inside an auto-created 'outputs' directory.
        """
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = f"outputs/{filename}_{timestamp}.{format_type}"

        try:
            if format_type.lower() == "json":
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(resources, f, indent=4)
                console.print(f"[bold green]✔ Report successfully exported to JSON: {filepath}[/bold green]")
                
            elif format_type.lower() == "csv":
                with open(filepath, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    # Header rows mapping the contract
                    writer.writerow(["Resource ID", "Resource Type", "Region", "Status", "Avg CPU", "Wasted Cost USD"])
                    
                    for res in resources:
                        metrics = res.get("metrics", {})
                        writer.writerow([
                            res["resource_id"],
                            res["resource_type"],
                            res["region"],
                            res["status"],
                            metrics.get("average_cpu", "N/A"),
                            metrics.get("wasted_cost_usd", 0.0)
                        ])
                console.print(f"[bold green]✔ Report successfully exported to CSV: {filepath}[/bold green]")
        except Exception as e:
            console.print(f"[bold red]❌ Failed to export report. Error: {str(e)}[/bold red]")


# --- Standalone Testing Block for Member 4 Complete Flow ---
if __name__ == "__main__":
    # Mocking Member 3's advanced dictionary data contract for final testing
    mock_scanned_data = [
        {
            "resource_id": "i-0abc1234def56789a",
            "resource_type": "EC2_INSTANCE",
            "region": "ap-south-1",
            "status": "running",
            "metrics": {
                "average_cpu": 1.45,
                "days_window": 14,
                "wasted_cost_usd": 60.80
            },
            "tags": {"Environment": "Dev", "Owner": "Yash"}
        },
        {
            "resource_id": "i-099988887777aaaa6",
            "resource_type": "EC2_INSTANCE",
            "region": "us-east-1",
            "status": "running",
            "metrics": {
                "average_cpu": 3.20,
                "days_window": 14,
                "wasted_cost_usd": 8.50
            },
            "tags": {"Environment": "Testing"}
        }
    ]
    
    # 1. Test terminal rendering dashboard
    ReportFormatter.display_terminal_report(mock_scanned_data)
    
    # 2. Test File Exports
    ReportFormatter.export_report(mock_scanned_data, format_type="json")
    ReportFormatter.export_report(mock_scanned_data, format_type="csv")