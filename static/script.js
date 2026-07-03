let network = null;

document.getElementById('upload-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = document.getElementById('scan-btn');
    btn.innerText = "PROCESSING PIPELINE...";
    
    // Using FormData to support both text and PDF uploads
    const formData = new FormData(e.target);

    try {
        const response = await fetch('http://127.0.0.1:5000/analyze', {
            method: 'POST',
            body: formData // No Content-Type header needed for FormData
        });

        const data = await response.json();
        if (data.error) throw new Error(data.error);
        
        renderGraph(data.nodes, data.edges);
        btn.innerText = "SCAN COMPLETE";
    } catch (err) {
        console.error(err);
        btn.innerText = "SYSTEM FAILURE";
    } finally {
        setTimeout(() => { btn.innerText = "EXECUTE FORENSICS"; }, 3000);
    }
});

function renderGraph(nodesArray, edgesArray) {
    const container = document.getElementById('mynetwork');
    const nodes = new vis.DataSet(nodesArray);
    const edges = new vis.DataSet(edgesArray);
    
    const options = {
        nodes: { shape: 'box', margin: 10, borderWidth: 2 },
        edges: { arrows: 'to', smooth: { type: 'cubicBezier', forceDirection: 'horizontal' } },
        layout: { hierarchical: { direction: 'LR', sortMethod: 'directed' } },
        physics: { enabled: false }
    };

    if (network) network.destroy();
    network = new vis.Network(container, { nodes, edges }, options);

    // NEW: Handle Node Clicks to open reasoning panel
    network.on("click", function (params) {
        if (params.nodes.length > 0) {
            const nodeId = params.nodes[0];
            const nodeData = nodes.get(nodeId);
            
            document.getElementById('inspector-panel').classList.remove('hidden');
            document.getElementById('report-content').innerText = nodeData.forensic_report || "Original Document Node";
            document.getElementById('node-text').innerText = nodeData.text_data;
        } else {
            document.getElementById('inspector-panel').classList.add('hidden');
        }
    });
}