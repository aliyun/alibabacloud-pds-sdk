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
    public class VideoMediaAudioStream : TeaModel {
        /// <summary>
        /// bit_rate 音频比特率 单位：bps
        /// </summary>
        [NameInMap("bit_rate")]
        [Validation(Required=false)]
        public string BitRate { get; set; }

        /// <summary>
        /// channel_layout 声道布局
        /// </summary>
        [NameInMap("channel_layout")]
        [Validation(Required=false)]
        public string ChannelLayout { get; set; }

        /// <summary>
        /// channels 音频数/声道数
        /// </summary>
        [NameInMap("channels")]
        [Validation(Required=false)]
        public long Channels { get; set; }

        /// <summary>
        /// code_name 音频编码模式
        /// </summary>
        [NameInMap("code_name")]
        [Validation(Required=false)]
        public string CodeName { get; set; }

        /// <summary>
        /// duration 单位 秒
        /// </summary>
        [NameInMap("duration")]
        [Validation(Required=false)]
        public string Duration { get; set; }

        /// <summary>
        /// sample_rate 音频采样率
        /// </summary>
        [NameInMap("sample_rate")]
        [Validation(Required=false)]
        public string SampleRate { get; set; }

    }

}
