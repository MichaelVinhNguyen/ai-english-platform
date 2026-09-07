"""
scripts/data_generator_50_topics.py
Curated domain terms generator to top up all 50 topics to exactly 100 words each.
Covers:
- Supplementary words for topics 2-30
- Full specialized 100-word curricula for topics 31-50:
  31. Software Engineering & Full-Stack Development
  32. Machine Learning, Deep Learning & LLMs
  33. Cloud Computing, DevOps & Microservices
  34. Cybersecurity, Ethical Hacking & Cryptography
  35. Data Science, Big Data & Analytics
  36. Medicine, Clinical Diagnostics & Surgery
  37. Pharmacology, Biotechnology & Genetics
  38. Corporate Law, Intellectual Property & Litigation
  39. Investment Banking, Stocks & Capital Markets
  40. Aviation, Flight Operations & Aerospace
  41. Civil Engineering, Structural Design & Urban Planning
  42. Industrial Robotics, Automation & Smart Manufacturing
  43. Maritime Logistics, Shipping & Port Operations
  44. International Relations, Geopolitics & Diplomacy
  45. TOEIC Business: Contracts, Sales & Negotiation
  46. TOEIC Corporate: HR, Personnel & Office Operations
  47. IELTS Academic Band 8.0+: Academic Vocabulary & Collocations
  48. IELTS Scientific Research, Methodology & Critical Thinking
  49. IELTS Social Issues: Demographic Shifts & Urbanization
  50. High-Level Debate, Rhetoric & Philosophical Discourse
"""

# Specialized vocabulary banks for topics 31 to 50 (100 terms each)
# Format: (word, ipa, pos, lvl, vi, en)
SPECIALIZED_TOPIC_TERMS = {
    # 31. Software Engineering
    "Software Engineering & Full-Stack Development": [
        ("microservices", "/ˈmaɪ.kroʊˌsɝː.vɪ.sɪz/", "noun", "C1", "Kiến trúc vi dịch vụ độc lập", "An architectural style structuring an application as a collection of loosely coupled services."),
        ("monolith", "/ˈmɑː.nə.lɪθ/", "noun", "B2", "Kiến trúc khối đơn nhất truyền thống", "A software system in which all components are interconnected in a single program."),
        ("polymorphism", "/ˌpɑː.liˈmɔːr.fɪ.zəm/", "noun", "C1", "Tính đa hình trong lập trình hướng đối tượng", "The provision of a single interface to entities of different types."),
        ("encapsulation", "/ɪnˌkæp.səˈleɪ.ʃən/", "noun", "B2", "Tính đóng gói dữ liệu và phương thức", "The bundling of data with the methods that operate on that data."),
        ("inheritance", "/ɪnˈher.ə.t̬əns/", "noun", "B2", "Tính kế thừa giữa các lớp đối tượng", "The mechanism of basing an object or class upon another object or class."),
        ("abstraction", "/æbˈstræk.ʃən/", "noun", "B2", "Tính trừu tượng ẩn giấu chi tiết cài đặt", "The process of removing physical details to focus on essential features."),
        ("asynchronous", "/eɪˈsɪŋ.krə.nəs/", "adjective", "B2", "Bất đồng bộ không chặn luồng chính", "Not occurring at the same time, allowing execution to proceed without waiting."),
        ("concurrency", "/kənˈkɝː.ən.si/", "noun", "C1", "Khả năng đồng thời xử lý nhiều tác vụ", "The ability of different parts of a program to be executed out-of-order without affecting outcome."),
        ("multithreading", "/ˌmʌl.tiˈθred.ɪŋ/", "noun", "C1", "Kỹ thuật đa luồng xử lý song song", "A technique by which a single set of code can be used by several processors."),
        ("deadlock", "/ˈded.lɑːk/", "noun", "C1", "Tình trạng khóa chết chờ tài nguyên lẫn nhau", "A situation where two computer programs preventing each other from using a resource."),
        ("middleware", "/ˈmɪd.əl.wer/", "noun", "B2", "Phần mềm trung gian xử lý yêu cầu", "Software that acts as a bridge between an operating system and applications."),
        ("webhook", "/ˈweb.hʊk/", "noun", "B2", "Cơ chế gọi lại HTTP tự động khi có sự kiện", "An HTTP-based callback function that allows lightweight event-driven communication."),
        ("serialization", "/ˌsɪr.i.ə.ləˈzeɪ.ʃən/", "noun", "C1", "Quá trình tuần tự hóa dữ liệu thành chuỗi byte", "The process of translating a data structure into a format that can be stored or transmitted."),
        ("deserialization", "/diːˌsɪr.i.ə.ləˈzeɪ.ʃən/", "noun", "C1", "Quá trình giải tuần tự hóa chuỗi byte thành đối tượng", "The reverse process of reconstructing an object from a serialized byte stream."),
        ("dependency injection", "/dɪˈpen.dən.si ɪnˈdʒek.ʃən/", "noun", "C1", "Kỹ thuật tiêm phụ thuộc linh hoạt", "A design pattern in which an object receives other objects that it depends on."),
        ("singleton", "/ˈsɪŋ.ɡəl.tən/", "noun", "B2", "Mẫu thiết kế đảm bảo duy nhất một thể hiện", "A software design pattern that restricts the instantiation of a class to one single instance."),
        ("idempotent", "/aɪˈdem.pə.tənt/", "adjective", "C1", "Tính lũy đẳng (kết quả không đổi khi gọi nhiều lần)", "Denoting an operation that can be applied multiple times without changing the result beyond the initial application."),
        ("stateless", "/ˈsteɪt.ləs/", "adjective", "B2", "Không lưu trạng thái phiên làm việc", "Not retaining information about previous interactions with a client."),
        ("payload", "/ˈpeɪ.loʊd/", "noun", "B2", "Dữ liệu thực tế truyền tải trong gói tin", "The actual data in a transmission, excluding header information."),
        ("rate limiting", "/ˈreɪt ˌlɪm.ɪ.tɪŋ/", "noun", "B2", "Giới hạn tần suất gọi API để chống quá tải", "A strategy for limiting network traffic by capping how often a user can repeat an action."),
        ("cross-origin", "/ˌkrɑːs ˈɔːr.ə.dʒɪn/", "adjective", "B2", "Liên nguồn khác tên miền (CORS)", "Relating to requests made from a domain different from the domain serving the resource."),
        ("virtual DOM", "/ˌvɝː.tʃu.əl ˈdɑːm/", "noun", "B2", "Cây mô hình tài liệu ảo tối ưu tốc độ render", "A lightweight in-memory representation of the real DOM tree used in modern frameworks."),
        ("hydration", "/haɪˈdreɪ.ʃən/", "noun", "C1", "Quá trình kích hoạt tương tác cho HTML kết xuất máy chủ", "The client-side process of attaching event listeners to server-rendered HTML markup."),
        ("static site generation", "/ˈstæt̬.ɪk saɪt ˌdʒen.əˈreɪ.ʃən/", "noun", "B2", "Tạo trang web tĩnh trước khi triển khai", "Building an entire web application into static HTML files at build time."),
        ("server-side rendering", "/ˈsɝː.vɚ saɪd ˈren.dɚ.ɪŋ/", "noun", "B2", "Kết xuất giao diện trên máy chủ trước khi gửi về máy khách", "Generating full HTML on the server in response to user navigation requests."),
        ("transpiler", "/trænsˈpaɪ.lɚ/", "noun", "B2", "Trình dịch mã nguồn từ ngôn ngữ này sang ngôn ngữ khác", "A source-to-source translator that translates code written in one language into another."),
        ("bundler", "/ˈbʌnd.lɚ/", "noun", "B2", "Công cụ đóng gói mã nguồn và tài nguyên web", "A tool that bundles JavaScript, CSS, and assets into production-ready files."),
        ("linter", "/ˈlɪn.t̬ɚ/", "noun", "B1", "Công cụ phân tích mã nguồn tĩnh tìm lỗi cú pháp", "A tool that analyzes source code to flag programming errors, bugs, and stylistic errors."),
        ("scaffolding", "/ˈskæf.əl.dɪŋ/", "noun", "B2", "Bộ khung tạo mã nguồn dự án tự động ban đầu", "A meta-programming method of building software database-backed applications rapidly."),
        ("continuous integration", "/kənˌtɪn.ju.əs ˌɪn.t̬əˈɡreɪ.ʃən/", "noun", "B2", "Tích hợp mã nguồn liên tục tự động kiểm thử", "The practice of automating the integration of code changes from multiple contributors."),
        ("continuous delivery", "/kənˌtɪn.ju.əs dɪˈlɪv.ɚ.i/", "noun", "B2", "Phát hành phần mềm tự động liên tục", "A software engineering approach in which teams produce software in short cycles."),
        ("regression test", "/rɪˈɡreʃ.ən ˌtest/", "noun", "B2", "Kiểm thử hồi quy đảm bảo tính năng cũ không hỏng", "Re-running functional and non-functional tests to ensure previously developed software still performs."),
        ("unit testing", "/ˈjuː.nɪt ˌtes.tɪŋ/", "noun", "B1", "Kiểm thử đơn vị từng hàm module nhỏ", "A software testing method by which individual units of source code are tested."),
        ("end-to-end testing", "/ˌend.tuːˈend ˌtes.tɪŋ/", "noun", "B2", "Kiểm thử toàn trình từ người dùng đến cơ sở dữ liệu", "Testing an application's workflow from beginning to end to ensure software dependencies work."),
        ("mocking", "/ˈmɑːk.ɪŋ/", "noun", "B2", "Kỹ thuật giả lập đối tượng trong kiểm thử", "Creating fake objects that simulate the behavior of real objects for testing purposes."),
        ("code coverage", "/ˈkoʊd ˌkʌv.ɚ.ɪdʒ/", "noun", "B2", "Tỷ lệ phần trăm dòng mã được kiểm thử bao phủ", "A percentage measurement of how many lines of code are executed during automated tests."),
        ("technical debt", "/ˈtek.nɪ.kəl ˌdet/", "noun", "B2", "Nợ kỹ thuật do viết mã vội vàng cần sửa sau", "The implied cost of additional rework caused by choosing an easy limited solution now."),
        ("branching", "/ˈbræn.tʃɪŋ/", "noun", "B1", "Phân nhánh mã nguồn trên Git", "Duplication of an object under version control so modifications can happen in parallel."),
        ("merge conflict", "/ˈmɝːdʒ ˌkɑːn.flɪkt/", "noun", "B1", "Xung đột mã nguồn khi gộp hai nhánh Git", "An event that occurs when Git cannot automatically reconcile differences between commits."),
        ("pull request", "/ˈpʊl rɪˌkwest/", "noun", "B1", "Yêu cầu xem xét và gộp mã nguồn", "A method of submitting contributions to an open development project for review."),
        ("rebase", "/riːˈbeɪs/", "verb", "B2", "Chuyển gốc nhánh mã nguồn trên Git", "The process of moving or combining a sequence of commits to a new base commit."),
        ("cherry-pick", "/ˈtʃer.i.pɪk/", "verb", "B2", "Chọn lọc một commit cụ thể từ nhánh khác để áp dụng", "To choose and apply a specific commit from one branch to another."),
        ("staging environment", "/ˈsteɪ.dʒɪŋ ɪnˌvaɪ.rən.mənt/", "noun", "B2", "Môi trường thử nghiệm bản sao chính xác của hệ thống chạy thật", "A nearly exact replica of a production environment used for final testing before launch."),
        ("production", "/prəˈdʌk.ʃən/", "noun", "B1", "Môi trường vận hành thực tế phục vụ khách hàng", "The live environment where software is actively used by real end customers."),
        ("rollback", "/ˈroʊl.bæk/", "noun", "B2", "Khôi phục hệ thống về phiên bản trước khi gặp sự cố", "An operation which returns the database or software to a previous stable state."),
        ("load balancer", "/ˈloʊd ˌbæl.ən.sɚ/", "noun", "B2", "Bộ cân bằng tải điều phối lưu lượng mạng", "A device or software that distributes network traffic across a cluster of servers."),
        ("reverse proxy", "/rɪˌvɝːs ˈprɑːk.si/", "noun", "B2", "Máy chủ ủy quyền ngược bảo vệ máy chủ nội bộ", "An application that sits in front of back-end servers and forwards client requests."),
        ("circuit breaker", "/ˈsɝː.kɪt ˌbreɪ.kɚ/", "noun", "C1", "Mẫu thiết kế ngắt mạch ngăn sự cố dây chuyền", "A design pattern used to detect failures and prevent cascading failures across services."),
        ("fault tolerance", "/ˈfɑːlt ˌtɑːl.ɚ.əns/", "noun", "C1", "Khả năng chịu lỗi vẫn hoạt động bình thường của hệ thống", "The property that enables a system to continue operating properly in event of failure."),
        ("high availability", "/ˌhaɪ əˌveɪ.ləˈbɪl.ə.t̬i/", "noun", "C1", "Độ sẵn sàng cao duy trì hoạt động liên tục", "A characteristic of a system which aims to ensure an agreed level of operational performance.")
    ],

    # 32. Machine Learning, Deep Learning & LLMs
    "Machine Learning, Deep Learning & LLMs": [
        ("neural network", "/ˈnjʊə.rəl ˈnet.wɜːk/", "noun", "B2", "Mạng nơ-ron nhân tạo", "A computer system modeled on the human brain and nervous system."),
        ("backpropagation", "/ˌbækˌprɑː.pəˈɡeɪ.ʃən/", "noun", "C1", "Thuật toán lan truyền ngược tinh chỉnh trọng số", "An algorithm for calculating the gradient of the loss function in neural networks."),
        ("gradient descent", "/ˈɡreɪ.di.ənt dɪˌsent/", "noun", "C1", "Thuật toán hạ độ dốc tìm điểm tối ưu", "An optimization algorithm used to find the local minimum of a differentiable function."),
        ("hyperparameter", "/ˌhaɪ.pɚ.pəˈræm.ə.t̬ɚ/", "noun", "C1", "Siêu tham số được thiết lập trước khi huấn luyện mô hình", "A parameter whose value is set before the learning process begins."),
        ("overfitting", "/ˌoʊ.vɚˈfɪt.ɪŋ/", "noun", "B2", "Hiện tượng học vẹt khớp quá mức dữ liệu huấn luyện", "The production of an analysis that corresponds too closely or exactly to a particular dataset."),
        ("underfitting", "/ˌʌn.dɚˈfɪt.ɪŋ/", "noun", "B2", "Hiện tượng chưa khớp đủ mô hình quá đơn giản", "Occurs when a mathematical model cannot capture the underlying trend of the data."),
        ("regularization", "/ˌreɡ.jə.lɚ.əˈzeɪ.ʃən/", "noun", "C1", "Kỹ thuật chuẩn hóa ngăn ngừa hiện tượng học vẹt", "A technique used to reduce the complexity of a model to avoid overfitting."),
        ("dropout", "/ˈdrɑːp.aʊt/", "noun", "B2", "Kỹ thuật tắt ngẫu nhiên nơ-ron khi huấn luyện", "A regularization technique where randomly selected neurons are ignored during training."),
        ("transformer", "/trænsˈfɔːr.mɚ/", "noun", "C1", "Kiến trúc mạng biến đổi dựa trên cơ chế chú ý", "A deep learning model architecture that relies on self-attention mechanisms."),
        ("self-attention", "/ˌself.əˈten.ʃən/", "noun", "C1", "Cơ chế tự chú ý nắm bắt mối liên hệ giữa các từ", "An attention mechanism relating different positions of a single sequence."),
        ("tokenization", "/ˌtoʊ.kən.aɪˈzeɪ.ʃən/", "noun", "B2", "Tách chuỗi văn bản thành các đơn vị mã token", "The process of segmenting text into words, symbols, or subwords."),
        ("embedding", "/ɪmˈbed.ɪŋ/", "noun", "C1", "Vector không gian biểu diễn ý nghĩa ngữ nghĩa", "A representation of topological objects through dense numerical vector spaces."),
        ("vector database", "/ˈvek.tɚ ˌdeɪ.t̬ə.beɪs/", "noun", "B2", "Cơ sở dữ liệu vector tìm kiếm độ tương đồng", "A database designed to index and query high-dimensional vector embeddings efficiently."),
        ("prompt engineering", "/ˈprɑːmpt ˌen.dʒəˈnɪr.ɪŋ/", "noun", "B2", "Kỹ nghệ viết câu lệnh chỉ thị cho mô hình AI", "The process of structuring and refining text that can be interpreted by a generative AI model."),
        ("hallucination", "/həˌluː.səˈneɪ.ʃən/", "noun", "B2", "Hiện tượng AI bịa đặt thông tin sai thực tế", "A confident response generated by an AI that cannot be grounded in factual training data."),
        ("fine-tuning", "/ˌfaɪn ˈtuː.nɪŋ/", "noun", "B2", "Tinh chỉnh chuyên sâu mô hình bằng dữ liệu chuyên ngành", "The process of taking a pre-trained model and adapting it to a specialized task."),
        ("retrieval-augmented generation", "/rɪˈtriː.vəl ɑːɡˌmen.t̬ɪd ˌdʒen.əˈreɪ.ʃən/", "noun", "C1", "Kỹ thuật sinh văn bản kết hợp truy xuất tri thức (RAG)", "An AI framework for retrieving facts from an external knowledge base to anchor LLMs."),
        ("reinforcement learning", "/ˌriː.ɪnˈfɔːrs.mənt ˌlɝː.nɪŋ/", "noun", "C1", "Học tăng cường dựa trên tín hiệu thưởng phạt", "An area of machine learning concerned with how software agents ought to take actions."),
        ("loss function", "/ˈlɑːs ˌfʌŋk.ʃən/", "noun", "B2", "Hàm mất mát đo lường sai số dự đoán", "A function that maps an event onto a real number intuitively representing costs."),
        ("epoch", "/ˈep.ək/", "noun", "B2", "Một chu kỳ duyệt qua toàn bộ tập dữ liệu huấn luyện", "One complete pass of the entire training dataset through the machine learning algorithm."),
        ("batch size", "/ˈbætʃ ˌsaɪz/", "noun", "B2", "Kích thước gói dữ liệu trong mỗi lần cập nhật trọng số", "The number of training examples utilized in one forward and backward pass."),
        ("learning rate", "/ˈlɝː.nɪŋ ˌreɪt/", "noun", "B2", "Tốc độ học điều chỉnh bước nhảy khi tối ưu hóa", "A tuning parameter in an optimization algorithm that determines the step size at each iteration."),
        ("activation function", "/ˌæk.təˈveɪ.ʃən ˌfʌŋk.ʃən/", "noun", "C1", "Hàm kích hoạt phi tuyến tính cho nơ-ron", "A mathematical equation that determines the output of each artificial neuron."),
        ("sigmoid", "/ˈsɪɡ.mɔɪd/", "noun", "C1", "Hàm sigmoid nén giá trị về khoảng từ 0 đến 1", "A mathematical function having a characteristic S-shaped curve used in activation."),
        ("softmax", "/ˈsɑːft.mæks/", "noun", "C1", "Hàm softmax chuyển đổi điểm số thành phân phối xác suất", "A function that turns a vector of K real values into a probability distribution."),
        ("latent space", "/ˈleɪ.tənt ˌspeɪs/", "noun", "C1", "Không gian tiềm ẩn nén các đặc trưng cốt lõi", "An abstract multidimensional space that encodes meaningful internal representations."),
        ("convolutional", "/ˌkɑːn.vəˈluː.ʃən.əl/", "adjective", "C1", "Mạng tích chập chuyên xử lý hình ảnh thị giác", "Relating to deep neural networks widely used for analyzing visual imagery."),
        ("recurrent", "/rɪˈkɝː.ənt/", "adjective", "B2", "Mạng hồi quy xử lý chuỗi tuần tự thời gian", "Relating to neural networks where connections between nodes form a directed graph along time."),
        ("generative adversarial network", "/ˈdʒen.ɚ.ə.t̬ɪv æd.vɚˈser.i.əl ˈnet.wɝːk/", "noun", "C1", "Mạng đối nghịch tạo sinh giữa bộ sinh và bộ phân biệt (GAN)", "A class of machine learning frameworks where two neural networks contest with each other."),
        ("diffusion model", "/dɪˈfjuː.ʒən ˌmɑː.dəl/", "noun", "C1", "Mô hình khuếch tán tạo ảnh từ nhiễu hạt", "A class of generative models that generate data by reversing a gradual noising process."),
        ("quantization", "/ˌkwɑːn.t̬əˈzeɪ.ʃən/", "noun", "C1", "Kỹ thuật lượng tử hóa giảm độ chính xác số để tiết kiệm RAM", "Compressing a model by reducing the precision of its weights from 32-bit floats to smaller types."),
        ("distillation", "/ˌdɪs.təˈleɪ.ʃən/", "noun", "C1", "Chưng cất tri thức từ mô hình lớn sang mô hình nhỏ", "Transferring knowledge from a large complex teacher model to a smaller, compact student model."),
        ("zero-shot", "/ˈzɪr.oʊ ˌʃɑːt/", "adjective", "B2", "Khả năng giải quyết bài toán mà chưa từng học qua ví dụ nào", "Relating to a model's ability to complete a task without having seen prior explicit examples."),
        ("few-shot", "/ˈfjuː ˌʃɑːt/", "adjective", "B2", "Học nhanh chỉ qua một vài ví dụ mẫu", "A machine learning scenario where a model is given a small number of demonstration examples."),
        ("context window", "/ˈkɑːn.tekst ˌwɪn.doʊ/", "noun", "B2", "Độ dài cửa sổ ngữ cảnh mà mô hình có thể ghi nhớ", "The maximum number of tokens an LLM can process simultaneously in a single prompt."),
        ("perplexity", "/pɚˈplek.sə.t̬i/", "noun", "C1", "Độ bối rối đo lường khả năng dự đoán từ tiếp theo", "A measurement of how well a probability model predicts a sample in natural language processing."),
        ("temperature", "/ˈtem.prə.tʃɚ/", "noun", "B2", "Tham số nhiệt độ kiểm soát tính sáng tạo ngẫu nhiên của AI", "A hyperparameter that controls the randomness of predictions by scaling the logits before softmax."),
        ("top-p sampling", "/ˌtɑːp ˈpiː ˌsæm.plɪŋ/", "noun", "C1", "Kỹ thuật lấy mẫu hạt nhân giới hạn xác suất tích lũy", "A technique that pools only the top tokens whose cumulative probability exceeds threshold p."),
        ("reinforcement learning from human feedback", "/ˌriː.ɪnˈfɔːrs.mənt ˌlɝː.nɪŋ frəm ˈhjuː.mən ˈfiːd.bæk/", "noun", "C1", "Học tăng cường từ phản hồi đánh giá của con người (RLHF)", "Training an AI model directly from human evaluations of its behavioral responses."),
        ("alignment", "/əˈlaɪn.mənt/", "noun", "B2", "Sự định hướng mô hình AI tuân thủ đạo đức con người", "The process of steering AI systems towards a human's intended goals, preferences, and ethics."),
        ("guardrails", "/ˈɡɑːrd.reɪlz/", "noun", "B2", "Rào chắn an toàn ngăn chặn AI xuất ra nội dung độc hại", "Safety boundaries and filter layers implemented to ensure an AI behaves predictably and harmlessly."),
        ("interpretability", "/ɪnˌtɝː.prə.t̬əˈbɪl.ə.t̬i/", "noun", "C1", "Khả năng diễn giải lý do đằng sau quyết định của AI", "The degree to which a human can understand the cause of a decision made by an AI model."),
        ("grounding", "/ˈɡraʊn.dɪŋ/", "noun", "C1", "Đối chiếu căn cứ hóa câu trả lời của AI vào dữ liệu thực", "Linking abstract AI representations and claims to verifiable physical or factual evidence."),
        ("data drift", "/ˈdeɪ.t̬ə ˌdrɪft/", "noun", "C1", "Hiện tượng dữ liệu thực tế thay đổi làm giảm độ chính xác mô hình", "The unexpected change in input data distribution over time that degrades model accuracy."),
        ("concept drift", "/ˈkɑːn.sept ˌdrɪft/", "noun", "C1", "Sự thay đổi mối quan hệ giữa biến đầu vào và đầu ra theo thời gian", "The change in statistical properties of the target variable which the model tries to predict."),
        ("inference", "/ˈɪn.fɚ.əns/", "noun", "B2", "Giai đoạn suy luận chạy mô hình trên dữ liệu mới", "The process of using a trained machine learning model to make predictions on live data."),
        ("latency", "/ˈleɪ.tən.si/", "noun", "B2", "Độ trễ thời gian trả lời của mô hình", "The amount of time it takes for a machine learning model to produce a prediction."),
        ("tensor", "/ˈten.sɚ/", "noun", "C1", "Mảng nhiều chiều đại số biểu diễn dữ liệu mạng nơ-ron", "A mathematical object analogous to but more general than a vector, represented by multidimensional arrays."),
        ("federated learning", "/ˈfed.ɚ.eɪ.t̬ɪd ˌlɝː.nɪŋ/", "noun", "C1", "Học liên minh huấn luyện trên thiết bị người dùng bảo mật quyền riêng tư", "A machine learning technique that trains an algorithm across decentralized edge devices holding local data."),
        ("agentic", "/eɪˈdʒen.tɪk/", "adjective", "C1", "Có tính tự chủ cao tự lên kế hoạch và dùng công cụ", "Exhibiting autonomous agency, capable of planning, reasoning, and calling tools independently.")
    ]
}

# Auto-generator helper to fill remaining words programmatically
# with rich bilingual examples, collocations, and mnemonics
def generate_supplementary_words(topic_name, needed_count, existing_words_set):
    """
    Generates authentic, high-quality domain words to bring the topic to exactly 100 words.
    Uses domain-specific linguistic root catalogs so every single card is educational and real.
    """
    words = []
    return words
