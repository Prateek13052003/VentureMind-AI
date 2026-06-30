"use client";

import { useState } from "react";
import api from "@/services/api";
import { StartupResponse } from "@/types/startup";

export default function StartupForm() {
    const [domain, setDomain] = useState("");
    const [problem, setProblem] = useState("");
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<StartupResponse | null>(null);

    const generateReport = async () => {
        try {
            setLoading(true);

            const res = await api.post("/generate-startup", {
                startup_domain: domain,
                problem_statement: problem,
            });

            setResult(res.data);
        } catch (err) {
            console.error(err);
            alert("Failed to generate report.");
        } finally {
            setLoading(false);
        }
    };
    const downloadPDF = async () => {
        if (!result) return;

        const response = await api.post(
            "/download-pdf",
            {
                investor_pitch: result.investor_pitch,
            },
            {
                responseType: "blob",
            }
        );

        const url = window.URL.createObjectURL(new Blob([response.data]));

        const link = document.createElement("a");
        link.href = url;
        link.download = "VentureMind_Report.pdf";
        link.click();

        window.URL.revokeObjectURL(url);
    };

    return (
        <div className="w-full max-w-4xl mx-auto mt-12 space-y-6">


            <input
                className="w-full rounded-xl border border-slate-700 bg-slate-800 text-white placeholder:text-slate-400 p-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Startup Domain"
                value={domain}
                onChange={(e) => setDomain(e.target.value)}
            />
            <textarea
                className="w-full rounded-xl border border-slate-700 bg-slate-800 text-white placeholder:text-slate-400 p-4 h-40 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Describe the problem..."
                value={problem}
                onChange={(e) => setProblem(e.target.value)}
            />

            <div className="flex gap-4">

                <button
                    onClick={generateReport}
                    disabled={loading}
                    className="bg-blue-600 hover:bg-blue-700 px-8 py-3 rounded-xl"
                >
                    {loading ? "Generating..." : "Generate Startup Report"}
                </button>

                {result && (
                    <button
                        onClick={downloadPDF}
                        className="bg-green-600 hover:bg-green-700 px-8 py-3 rounded-xl"
                    >
                        📄 Download PDF
                    </button>
                )}

            </div>


            {result && (
                <pre className="bg-slate-900 p-6 rounded-xl overflow-auto whitespace-pre-wrap">
                    {result.investor_pitch}
                </pre>
            )}

        </div>
    );
}