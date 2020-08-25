// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * play_media request
     */
    public class PlayMediaRequest : TeaModel {
        /// <summary>
        /// auth_key
        /// </summary>
        [NameInMap("AuthKey")]
        [Validation(Required=true, Pattern="[a-z0-9]+")]
        public string AuthKey { get; set; }

        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("DriveID")]
        [Validation(Required=true, Pattern="[0-9]+")]
        public string DriveID { get; set; }

        /// <summary>
        /// file_id
        /// </summary>
        [NameInMap("FileID")]
        [Validation(Required=true, MaxLength=50, Pattern="[a-z0-9.-_]{1,50}")]
        public string FileID { get; set; }

    }

}
