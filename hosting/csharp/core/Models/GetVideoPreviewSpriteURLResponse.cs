// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 获取视频雪碧图地址 url response
     */
    public class GetVideoPreviewSpriteURLResponse : TeaModel {
        /// <summary>
        /// col
        /// </summary>
        [NameInMap("col")]
        [Validation(Required=false)]
        public long Col { get; set; }

        /// <summary>
        /// count
        /// </summary>
        [NameInMap("count")]
        [Validation(Required=false)]
        public long Count { get; set; }

        /// <summary>
        /// frame_count
        /// </summary>
        [NameInMap("frame_count")]
        [Validation(Required=false)]
        public long FrameCount { get; set; }

        /// <summary>
        /// frame_height
        /// </summary>
        [NameInMap("frame_height")]
        [Validation(Required=false)]
        public long FrameHeight { get; set; }

        /// <summary>
        /// frame_width
        /// </summary>
        [NameInMap("frame_width")]
        [Validation(Required=false)]
        public long FrameWidth { get; set; }

        /// <summary>
        /// row
        /// </summary>
        [NameInMap("row")]
        [Validation(Required=false)]
        public long Row { get; set; }

        /// <summary>
        /// sprite_url_list
        /// </summary>
        [NameInMap("sprite_url_list")]
        [Validation(Required=false)]
        public List<string> SpriteUrlList { get; set; }

    }

}
