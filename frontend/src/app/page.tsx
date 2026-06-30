import StartupForm from "@/components/StartupForm";

export default function Home() {
    return (
        <main className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-black text-white py-20 px-6">

            <div className="max-w-6xl mx-auto text-center">

                <h1 className="text-6xl font-bold">
                    VentureMind AI 🚀
                </h1>

                <p className="mt-6 text-xl text-gray-300">
                    Turn your startup idea into an investor-ready report using AI agents.
                </p>

            </div>

            <StartupForm />

        </main>
    );
}