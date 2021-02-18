<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * play_media request.
 */
class PlayMediaRequest extends Model
{
    /**
     * @description auth_key
     *
     * @example zzsdfwiskaksfeewasdf001
     *
     * @var string
     */
    public $AuthKey;

    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $DriveID;

    /**
     * @description file_id
     *
     * @var string
     */
    public $FileID;
    protected $_name = [
        'AuthKey' => 'AuthKey',
        'DriveID' => 'DriveID',
        'FileID'  => 'FileID',
    ];

    public function validate()
    {
        Model::validateRequired('AuthKey', $this->AuthKey, true);
        Model::validateRequired('DriveID', $this->DriveID, true);
        Model::validateRequired('FileID', $this->FileID, true);
        Model::validatePattern('AuthKey', $this->AuthKey, '[a-z0-9]+');
        Model::validatePattern('DriveID', $this->DriveID, '[0-9]+');
        Model::validatePattern('FileID', $this->FileID, '[a-z0-9.-_]{1,50}');
        Model::validateMaxLength('FileID', $this->FileID, 50);
        Model::validateMinLength('FileID', $this->FileID, 40);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->AuthKey) {
            $res['AuthKey'] = $this->AuthKey;
        }
        if (null !== $this->DriveID) {
            $res['DriveID'] = $this->DriveID;
        }
        if (null !== $this->FileID) {
            $res['FileID'] = $this->FileID;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return PlayMediaRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['AuthKey'])) {
            $model->AuthKey = $map['AuthKey'];
        }
        if (isset($map['DriveID'])) {
            $model->DriveID = $map['DriveID'];
        }
        if (isset($map['FileID'])) {
            $model->FileID = $map['FileID'];
        }

        return $model;
    }
}
