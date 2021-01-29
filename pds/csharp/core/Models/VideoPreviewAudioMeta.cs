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
    public class VideoPreviewAudioMeta : TeaModel {
        /// <summary>
        /// bitrate
        /// </summary>
        [NameInMap("bitrate")]
        [Validation(Required=false)]
        public double? Bitrate { get; set; }

        /// <summary>
        /// channels
        /// </summary>
        [NameInMap("channels")]
        [Validation(Required=false)]
        public long? Channels { get; set; }

        /// <summary>
        /// duration
        /// </summary>
        [NameInMap("duration")]
        [Validation(Required=false)]
        public double? Duration { get; set; }

        /// <summary>
        /// sample_rate
        /// </summary>
        [NameInMap("sample_rate")]
        [Validation(Required=false)]
        public double? SampleRate { get; set; }

    }

}
