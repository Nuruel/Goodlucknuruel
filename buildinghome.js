document.getElementById('plot-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const location = document.getElementById('location').value;
    const region = document.getElementById('region').value;
    const budget = document.getElementById('budget').value;
    const size = document.getElementById('size').value;
    const nearSchool = document.getElementById('near-school').value;
    const nearHospital = document.getElementById('near-hospital').value;
    const publicTransport = document.getElementById('public-transport').value;

    const results = document.getElementById('results');
    results.innerHTML = `
        <h2>Matching Plots</h2>
        <p>Location: ${location}</p>
        <p>Region: ${region}</p>
        <p>Budget: ${budget}</p>
        <p>Size: ${size} sq ft</p>
        <p>Near School: ${nearSchool}</p>
        <p>Near Hospital: ${nearHospital}</p>
        <p>Public Transport: ${publicTransport}</p>
    `;

    // Here you would add the logic to fetch and display actual matching plots based on the user inputs.
});
