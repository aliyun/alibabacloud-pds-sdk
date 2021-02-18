<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Get story detail request.
 */
class GetStoryDetailRequest extends Model
{
    public $headers;

    /**
     * @description drive_id
     *
     * @example "101"
     *
     * @var string
     */
    public $driveId;

    /**
     * @description story_id
     *
     * @example "story112312"
     *
     * @var string
     */
    public $storyId;

    /**
     * @description url_expire_sec
     *
     * @example 900
     *
     * @var int
     */
    public $videoUrlExpireSec;
    protected $_name = [
        'driveId'           => 'drive_id',
        'storyId'           => 'story_id',
        'videoUrlExpireSec' => 'video_url_expire_sec',
    ];
    protected $_default = [
        'videoUrlExpireSec' => 900,
    ];

    public function validate()
    {
        Model::validateRequired('driveId', $this->driveId, true);
        Model::validateRequired('storyId', $this->storyId, true);
        Model::validatePattern('driveId', $this->driveId, '[0-9]+');
        Model::validateMaximum('videoUrlExpireSec', $this->videoUrlExpireSec, 14400);
        Model::validateMinimum('videoUrlExpireSec', $this->videoUrlExpireSec, 10);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->storyId) {
            $res['story_id'] = $this->storyId;
        }
        if (null !== $this->videoUrlExpireSec) {
            $res['video_url_expire_sec'] = $this->videoUrlExpireSec;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetStoryDetailRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['story_id'])) {
            $model->storyId = $map['story_id'];
        }
        if (isset($map['video_url_expire_sec'])) {
            $model->videoUrlExpireSec = $map['video_url_expire_sec'];
        }

        return $model;
    }
}
