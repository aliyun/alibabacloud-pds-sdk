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
    public class VideoMediaVideoStream : TeaModel {
        /// <summary>
        /// bitrate 视频比特率 单位：bps
        /// </summary>
        [NameInMap("bitrate")]
        [Validation(Required=false)]
        public string Bitrate { get; set; }

        /// <summary>
        /// clarity 清晰度（扫描）
        /// </summary>
        [NameInMap("clarity")]
        [Validation(Required=false)]
        public string Clarity { get; set; }

        /// <summary>
        /// code_name 视频编码模式
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
        /// fps 视频平均帧率
        /// </summary>
        [NameInMap("fps")]
        [Validation(Required=false)]
        public string Fps { get; set; }

        /// <summary>
        /// rotate 视频横屏 竖屏
        /// </summary>
        [NameInMap("rotate")]
        [Validation(Required=false)]
        public string Rotate { get; set; }

    }

}
