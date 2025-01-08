document.addEventListener("DOMContentLoaded", () => {
    // Fetch data from the Flask API
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            // Status Overview Chart
            const statusCtx = document.getElementById("statusChart").getContext("2d");
            new Chart(statusCtx, {
                type: "doughnut",
                data: {
                    labels: ["Done", "In Progress", "On Hold", "Under Review"],
                    datasets: [{
                        data: data.status_data,
                        backgroundColor: ["#4CAF50", "#FF9800", "#FFC107", "#03A9F4"]
                    }]
                }
            });

            // Priority Breakdown Chart
            const priorityCtx = document.getElementById("priorityChart").getContext("2d");
            new Chart(priorityCtx, {
                type: "bar",
                data: {
                    labels: ["Critical", "High", "Medium", "Low"],
                    datasets: [{
                        label: "Priority",
                        data: data.priority_data,
                        backgroundColor: ["#FF5722", "#FF9800", "#FFC107", "#03A9F4"]
                    }]
                }
            });

            // Team Workload Chart
            const workloadCtx = document.getElementById("workloadChart").getContext("2d");
            new Chart(workloadCtx, {
                type: "horizontalBar",
                data: {
                    labels: data.team_labels,
                    datasets: [{
                        label: "Workload",
                        data: data.workload_data,
                        backgroundColor: ["#8BC34A", "#03A9F4"]
                    }]
                },
                options: {
                    indexAxis: 'y'
                }
            });
        });
});
