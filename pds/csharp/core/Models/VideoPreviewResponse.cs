// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class VideoPreviewResponse : TeaModel {
        /// <summary>
        /// audio_channels
        /// </summary>
        [NameInMap("audio_channels")]
        [Validation(Required=false)]
        public long? AudioChannels { get; set; }

        /// <summary>
        /// audio_format
        /// </summary>
        [NameInMap("audio_format")]
        [Validation(Required=false)]
        public string AudioFormat { get; set; }

        [NameInMap("audio_meta")]
        [Validation(Required=false)]
        public VideoPreviewAudioMeta AudioMeta { get; set; }

        [NameInMap("audio_music_meta")]
        [Validation(Required=false)]
        public VideoPreviewAudioMusicMeta AudioMusicMeta { get; set; }

        /// <summary>
        /// audio_sample_rate
        /// </summary>
        [NameInMap("audio_sample_rate")]
        [Validation(Required=false)]
        public string AudioSampleRate { get; set; }

        /// <summary>
        /// audio_template_list
        /// </summary>
        [NameInMap("audio_template_list")]
        [Validation(Required=false)]
        public List<VideoPreviewTranscode> AudioTemplateList { get; set; }

        /// <summary>
        /// bitrate
        /// </summary>
        [NameInMap("bitrate")]
        [Validation(Required=false)]
        public string Bitrate { get; set; }

        /// <summary>
        /// duration
        /// </summary>
        [NameInMap("duration")]
        [Validation(Required=false)]
        public string Duration { get; set; }

        /// <summary>
        /// frame_rate
        /// </summary>
        [NameInMap("frame_rate")]
        [Validation(Required=false)]
        public string FrameRate { get; set; }

        /// <summary>
        /// height
        /// </summary>
        [NameInMap("height")]
        [Validation(Required=false)]
        public long? Height { get; set; }

        [NameInMap("sprite_info")]
        [Validation(Required=false)]
        public VideoPreviewSprite SpriteInfo { get; set; }

        /// <summary>
        /// template_list
        /// </summary>
        [NameInMap("template_list")]
        [Validation(Required=false)]
        public List<VideoPreviewTranscode> TemplateList { get; set; }

        /// <summary>
        /// thumbnail
        /// </summary>
        [NameInMap("thumbnail")]
        [Validation(Required=false)]
        public string Thumbnail { get; set; }

        /// <summary>
        /// video_format
        /// </summary>
        [NameInMap("video_format")]
        [Validation(Required=false)]
        public string VideoFormat { get; set; }

        /// <summary>
        /// width
        /// </summary>
        [NameInMap("width")]
        [Validation(Required=false)]
        public long? Width { get; set; }

    }

}
