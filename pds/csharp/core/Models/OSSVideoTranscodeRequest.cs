// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 启动视频转码请求
     */
    public class OSSVideoTranscodeRequest : TeaModel {
        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        /// <summary>
        /// file_path
        /// </summary>
        [NameInMap("file_path")]
        [Validation(Required=true, MaxLength=1000)]
        public string FilePath { get; set; }

        /// <summary>
        /// hls_time
        /// </summary>
        [NameInMap("hls_time")]
        [Validation(Required=false)]
        public long? HlsTime { get; set; }

        /// <summary>
        /// protection_scheme
        /// </summary>
        [NameInMap("protection_scheme")]
        [Validation(Required=false)]
        public string ProtectionScheme { get; set; }

        /// <summary>
        /// remarks
        /// </summary>
        [NameInMap("remarks")]
        [Validation(Required=false)]
        public string Remarks { get; set; }

        /// <summary>
        /// share_id
        /// </summary>
        [NameInMap("share_id")]
        [Validation(Required=false, Pattern="[0-9a-zA-Z-]+")]
        public string ShareId { get; set; }

        /// <summary>
        /// transcode
        /// </summary>
        [NameInMap("transcode")]
        [Validation(Required=false)]
        public bool? Transcode { get; set; }

    }

}
