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
    public class VideoPreviewAudioMusicMeta : TeaModel {
        /// <summary>
        /// album
        /// </summary>
        [NameInMap("album")]
        [Validation(Required=false)]
        public string Album { get; set; }

        /// <summary>
        /// artist
        /// </summary>
        [NameInMap("artist")]
        [Validation(Required=false)]
        public string Artist { get; set; }

        /// <summary>
        /// cover_url
        /// </summary>
        [NameInMap("cover_url")]
        [Validation(Required=false)]
        public string CoverUrl { get; set; }

        /// <summary>
        /// title
        /// </summary>
        [NameInMap("title")]
        [Validation(Required=false)]
        public string Title { get; set; }

    }

}
