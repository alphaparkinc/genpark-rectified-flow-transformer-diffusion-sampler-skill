from client import RectifiedFlowTransformerDiffusionSamplerClient

def main():
    client = RectifiedFlowTransformerDiffusionSamplerClient()
    res = client.sample_rectified_flow_latent('Futuristic architectural render of a vertical forest skyscraper at twilight', 16)
    print('Flux DiT Sampler: ' + res['sampling_job_id'] + ' (' + str(res['dit_layers_traversed']) + ' DiT layers)')
    print('Trajectory Linearity: ' + str(res['flow_trajectory_linearity_score']) + ' | Text Alignment: ' + str(res['text_alignment_clip_score_pct']) + '%')
    print('Inference Latency: ' + str(res['inference_latency_ms']) + 'ms')
    print('Image Output: ' + res['rendered_image_url'])

if __name__ == '__main__':
    main()
